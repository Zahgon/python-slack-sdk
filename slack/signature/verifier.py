import hashlib
import hmac
from time import time
from typing import Dict, Optional, Union


class Clock:
    @staticmethod
    def now() -> float:
        pass


class SignatureVerifier:
    def __init__(self, signing_secret: str, clock: Clock = Clock()):
        """Slack request signature verifier

        Slack signs its requests using a secret that's unique to your app.
        With the help of signing secrets, your app can more confidently verify
        whether requests from us are authentic.
        https://docs.slack.dev/authentication/verifying-requests-from-slack/
        """
        self.signing_secret = signing_secret
        self.clock = clock

    def is_valid_request(
        self,
        body: Union[str, bytes],
        headers: Dict[str, str],
    ) -> bool:
        """Verifies if the given signature is valid"""
        pass

    def is_valid(
        self,
        body: Union[str, bytes],
        timestamp: str,
        signature: str,
    ) -> bool:
        """Verifies if the given signature is valid"""
        pass

    def generate_signature(self, *, timestamp: str, body: Union[str, bytes]) -> Optional[str]:
        """Generates a signature"""
        pass
