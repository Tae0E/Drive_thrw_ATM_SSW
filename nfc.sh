#!/bin/sh
while [ 1 ]:
do
	(cd ~/libnfc/examples
	nfc-poll
	python sendnfc.py)
done
echo "done"
