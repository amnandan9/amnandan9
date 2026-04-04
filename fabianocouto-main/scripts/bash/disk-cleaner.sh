#!/bin/bash
SIZE=$(df -h / | awk 'NR==2 {print $2}')
USED=$(df -h / | awk 'NR==2 {print $3}')
AVAIL=$(df -h / | awk 'NR==2 {print $4}')
USAGE_PERCENTAGE=$(df -h / | awk 'NR==2 {print $5}')

echo "Total size: $SIZE"
echo "Available space: $AVAIL"
echo "Used space: $USED"
echo "Usage percentage: $USAGE_PERCENTAGE"

# SET THRESHOLD
if [ "$(echo $USAGE_PERCENTAGE | tr -d '%')" -gt 30 ]; then
  echo "Warning: High disk usage!"
  echo "Cleaning up disk space..."
  # Add your cleanup commands here
fi