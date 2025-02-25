---
#!/bin/bash
sudo gitlab-ctl registry-garbage-collect --delete-untagged > /var/log/gitlab-registry-cleanup.log