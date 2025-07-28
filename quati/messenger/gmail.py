import mimetypes
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from importlib.resources import files

# Path to logo image used in the email
LOGO_IMG = files("assets").joinpath("quati.gif")

# SMTP configuration
SMTP_PORT = 587
SMTP_HOST = "smtp.gmail.com"

# Supported message types and their styles
TYPES = ["error", "important", "note", "tip", "warning"]
TYPES_STYLES = {
    "error": {"bg_color": "#DB4A32", "icon": "⛔", "label": "Error"},
    "important": {"bg_color": "#bc00f5", "icon": "💬", "label": "Important"},
    "note": {"bg_color": "#523af5", "icon": "ℹ️", "label": "Note"},
    "tip": {"bg_color": "#00d357", "icon": "💡", "label": "Tip"},
    "warning": {"bg_color": "#F6B800", "icon": "⚠️", "label": "Warning"},
}


class EmailAlert:
    """
    Class for sending alert emails with custom HTML and attachment support.

    Allows you to configure a sender user, authentication token, and default recipient list.
    Uses SMTP with STARTTLS for secure sending.

    Args
    ----
    - `user` (str): Sender's email address.
    - `token` (str): Sender's app token or password (e.g., Gmail).
    - `receivers` (list[str]): Default recipient list

    Example
    -------
    ```
        emailer = EmailAlert("my_email@gmail.com", "password123", ["dest1@gmail.com"])
        emailer.send_email(title="Error", message="Something went wrong", type="error")
    ```
    """

    def __init__(self, user: str, token: str, receivers: list[str]):
        # Sender email address and token
        self.user = user
        self.token = token
        # Default recipients list
        self.receivers = receivers

    def send_email(
        self,
        abstract: str = "Abstract N/D",
        title: str = "Email Alert",
        datetime: str = "Datetime N/D",
        message: str = "Message N/D",
        context: str = "Context N/D",
        metadata: dict = None,
        attach: list[str] = [],
        type: str = "error",
        to: list[str] = None,
    ):
        # Validate alert type
        if type not in TYPES:
            raise ValueError(f"Invalid type: {type}. Must be one of {TYPES}")

        # Retrieve style info for given type
        t = TYPES_STYLES[type]
        color, ico, lbl = t["bg_color"], t["icon"], t["label"]
        subject = f"Alert Notification - {title}, {ico} {lbl}"

        # Highlight section of email
        highlight = f"""
            <p style="color: {color};"><b>{ico} {lbl}</b></p>
            <b>Summary:</b> {abstract};<br>
            <div class="log"><pre><code>{message}</code></pre></div>
        """

        # Render metadata as HTML
        metadata_html = ""
        if metadata:
            for k, v in metadata.items():
                metadata_html += f"<b>{k}:</b> {v};<br>"

        # HTML header and inline CSS
        html_head = f"""
            <head>
                <meta charset="UTF-8">
                <title>quati Email</title>
                <style>
                    body {{font-family: Arial, sans-serif; background: #f4f4f4; font-size: 12px;}}
                    .container {{width: 80%; margin: 20px auto; padding: 20px; border-radius: 25px; background: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.1);}}
                    .logo {{text-align: center; margin: 20px 0;}}
                    .logo img {{max-width: 200px;}}
                    .header {{font-size: x-large; text-align: center; background: {color}; color: #fff; padding: 20px; border-radius: 15px;}}
                    .log {{background: #f5f5f5; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin: 20px 0; overflow-x: auto;}}
                    .highlight {{border-left: 3.5px solid {color}; padding-left: 10px}}
                    .signature {{color: #9D9DA7; padding: 0 0 20px; text-align: center;}}
                </style>
            </head>
        """

        # HTML email body content
        html_body = f"""
            <body style="color: #464646;">
                <div class="logo"><img src="cid:logo" alt="Company Logo"></div>
                <div class="container">
                    <div class="header">🚨 {title}</div>
                    <p>Hello,<br>We have a new notification that may need your attention:</p>
                    <hr>
                    <div class="content">
                        <b>Datetime:</b> {datetime};<br>
                        <b>Context:</b> {context};<br>
                        {metadata_html}
                        <hr>
                        <div class="highlight">{highlight}</div>
                    </div>
                    <p style="text-align: center;">Thank you for your attention!</p>
                </div>
                <div class="signature">
                    System Notification<br>
                    <i>This is an automated email. Do not reply.</i>
                </div>
            </body>
        """

        # Full HTML structure
        msg_html = f"<!DOCTYPE html><html lang='en'>{html_head}{html_body}</html>"

        # Construct the multipart email object
        msg = MIMEMultipart("related")
        msg["Subject"] = subject
        msg["From"] = self.user
        msg["To"] = ", ".join(to or self.receivers)
        msg.attach(MIMEText(msg_html, "html"))

        # Add embedded logo image to email
        with open(LOGO_IMG, "rb") as f:
            img = MIMEBase("image", "png")
            img.set_payload(f.read())
            encoders.encode_base64(img)
            img.add_header("Content-ID", "<logo>")
            img.add_header("Content-Disposition", "inline", filename="logo.png")
            msg.attach(img)

        # Attach additional files, if any
        for filepath in attach:
            mime_type, _ = mimetypes.guess_type(filepath)
            mime_type = mime_type or "application/octet-stream"
            main_type, sub_type = mime_type.split("/", 1)

            with open(filepath, "rb") as f:
                part = MIMEBase(main_type, sub_type)
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={filepath.split('/')[-1]}")
                msg.attach(part)

        # Connect to SMTP server and send the email
        with smtplib.SMTP(f"{SMTP_HOST}:{SMTP_PORT}") as email:
            email.starttls()  # Secure the connection
            email.login(self.user, self.token)
            email.sendmail(self.user, to or self.receivers, msg.as_string().encode("utf-8"))
