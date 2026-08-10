import asyncio
import logging
import random
from dataclasses import dataclass
from typing import Awaitable, Callable, Generic, TypeVar

T = TypeVar("T")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


@dataclass
class TaskResult(Generic[T]):
    task_id: int
    result: T | None
    error: Exception | None = None


class AsyncTaskManager(Generic[T]):
    def __init__(self, workers: int = 4, retries: int = 3):
        self.workers = workers
        self.retries = retries
        self.queue: asyncio.Queue[tuple[int, Callable[[], Awaitable[T]]]] = (
            asyncio.Queue()
        )

    async def add_task(
        self,
        task_id: int,
        task: Callable[[], Awaitable[T]]
    ) -> None:
        await self.queue.put((task_id, task))

    async def worker(self, worker_id: int) -> None:
        while True:
            task_id, task = await self.queue.get()

            try:
                for attempt in range(1, self.retries + 1):
                    try:
                        logging.info(
                            "Worker %d running task %d (attempt %d)",
                            worker_id,
                            task_id,
                            attempt
                        )

                        result = await task()

                        logging.info(
                            "Task %d completed: %s",
                            task_id,
                            result
                        )
                        break

                    except Exception as exc:
                        logging.warning(
                            "Task %d failed: %s",
                            task_id,
                            exc
                        )

                        if attempt == self.retries:
                            logging.error(
                                "Task %d permanently failed",
                                task_id
                            )

                        await asyncio.sleep(0.5 * attempt)

            finally:
                self.queue.task_done()

    async def run(self) -> None:
        workers = [
            asyncio.create_task(self.worker(i))
            for i in range(1, self.workers + 1)
        ]

        await self.queue.join()

        for worker in workers:
            worker.cancel()

        await asyncio.gather(*workers, return_exceptions=True)


async def simulated_task(task_id: int) -> str:
    await asyncio.sleep(random.uniform(0.5, 2.0))

    if random.random() < 0.2:
        raise RuntimeError(f"Random failure in task {task_id}")

    return f"Task {task_id} finished successfully"


async def main() -> None:
    manager = AsyncTaskManager[str](
        workers=4,
        retries=3
    )

    for task_id in range(1, 11):
        await manager.add_task(
            task_id,
            lambda task_id=task_id: simulated_task(task_id)
        )

    await manager.run()

    print("\nAll tasks processed.")


if __name__ == "__main__":
    asyncio.run(main())