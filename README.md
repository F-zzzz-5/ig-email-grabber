# IG Email Grabber

Just incase the title is slightly misleading, please read the following points which will further explain how this works and its limitations.

## About
* Utilizes Instagram "Reset Password" API endpoint.
* Fetches email from HTTP response content.
* Email is partly hidden due to Instagram not sending back the entire email.

## How is this useful?
* Assists with OSINT operations.
* Completely anonymous assuming proxies.txt is used.

## Example Formatting
Instagram passes back a modified version of the email, with the first letter showing with the email provider.
```
s******@outlook.com
g********@yahoo.com
v****@gmail.com
```
