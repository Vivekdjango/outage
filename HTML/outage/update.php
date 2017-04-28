<?php
if($_POST["action1"]) {
include('/cgi-bin/outage/update.py');
}
//You can do an else, but I prefer a separate statement
if($_POST["action2"]) {
include('/cgi-bin/outage/mail_update.py');
}
?>
