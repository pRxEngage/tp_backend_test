from celery import shared_task


@shared_task
def import_upload_task(upload_task_id: int) -> None:
    """Candidate TODO: import studies for this upload task outside the request cycle."""
    msg = (
        "Assessment task placeholder: implement CSV parsing, CT.gov API fetching, "
        "fault-tolerant retries, upserts, progress tracking, and import metadata."
    )
    raise NotImplementedError(msg)
