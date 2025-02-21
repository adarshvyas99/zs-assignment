Problem: Registry space optimization and cleanup.

Goal: The GitLab container storage for images regularly consumes excessive storage on the
maintenance system and requires manual clearing. Implement a sustainable solution to
manage container image storage, automate cleanup, and prevent storage overrun.

Subtasks:
1. Deploy gitlab as docker container(standalone) with appropriate docker-compose file
and following:
2. Persistent storage 5G
3. Additional persistent storage for container registry 5G to hold docker images.
4. Image Expiration Policies. This should be configurable in terms of days.
5. Garbage Collection: Cron based automation to reclaim occupied space by deleted
images.
6. Notifications: Implement a monitoring and notification mechanism to send notifs for
all actions(disk 70% full, 90% full, cleaning up started/finished, disk space reclaimed
start/end)
7. Any additional optimizations should be listed in a document for future use-case.