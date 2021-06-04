!#bin/sh

/usr/bin/restic -r $RESTIC_REPOSITORY --password-file /bin/exchange/rpass backup /bin/exchange/*.csv --exclude='\bin \exchange' 