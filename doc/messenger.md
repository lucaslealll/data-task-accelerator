# Messengers & Alerts

Provides a class to send styled alerts and informational emails from just a few lines of code.

> [!NOTE]
> ```py
> from quati.messenger.gmail import EmailAlert
> ```

- [`EmailAlert`](#emailalert-class): Class to send HTML alert emails (types: error, tip, note, important, warning) with detailed context, attachments and metadata.
- [`send_email()`](#send_email-method): Method of `EmailAlert` to trigger the actual sending of the email.

---

### `EmailAlert` class

The `EmailAlert` class allows you to configure a sender (`user`, `token`) and default recipients. It sends a rich HTML-formatted alert email with metadata, attachments, and styling based on the type of alert.

#### Initialize email sender
```py
emailer = EmailAlert(
    user="your_email@gmail.com",
    token="your_app_token",
    receivers=["team@example.com", "devops@example.com"]
)
```

### `send_email()` method
The `send_email()` method sends a formatted alert email based on the provided type (`error`, `important,` `note`, `tip`, or `warning`), including optional metadata and attachments.

#### Parameters:
- `abstract` (`str`): Short summary of the alert
- `title` (`str`): Email subject/title
- `datetime` (`str`): When the event occurred
- `message` (`str`): Detailed log or traceback
- `context` (`str`): Name of the process or module
- `metadata` (`dict`, optional): Key-value pairs shown in the email
- `attach` (`list[str]`, optional): List of file paths to attach
- `type` (`str`): One of error, tip, note, important, warning
- `to` (`list[str]`, optional): Override recipient list

```py
emailer.send_email(
    abstract=repr(e),
    title="Data Pipeline Alert",
    datetime="2025-07-27 10:00",
    message=format_exc(),
    context="load_stage",
    metadata={"Pipeline": "Sales ETL", "Severity": "High"},
    attach=["../file.json", "../image.jpeg"],
    type="error"
)
```
