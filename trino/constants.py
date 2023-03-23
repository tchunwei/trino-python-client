# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Optional
import os

flavour = 'Presto' if os.environ.get('PRESTO_FLAVOUR', 'hetu') else 'Trino'

DEFAULT_PORT = 8080
DEFAULT_TLS_PORT = 443
DEFAULT_SOURCE = f"{flavour}-python-client"
DEFAULT_CATALOG: Optional[str] = None
DEFAULT_SCHEMA: Optional[str] = None
DEFAULT_AUTH: Optional[Any] = None
DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_REQUEST_TIMEOUT: float = 30.0

HTTP = "http"
HTTPS = "https"

URL_STATEMENT_PATH = "/v1/statement"

HEADER_CATALOG = f"X-{flavour}-Catalog"
HEADER_SCHEMA = f"X-{flavour}-Schema"
HEADER_SOURCE = f"X-{flavour}-Source"
HEADER_USER = f"X-{flavour}-User"
HEADER_CLIENT_INFO = f"X-{flavour}-Client-Info"
HEADER_CLIENT_TAGS = f"X-{flavour}-Client-Tags"
HEADER_EXTRA_CREDENTIAL = f"X-{flavour}-Extra-Credential"
HEADER_TIMEZONE = f"X-{flavour}-Time-Zone"

HEADER_SESSION = f"X-{flavour}-Session"
HEADER_SET_SESSION = f"X-{flavour}-Set-Session"
HEADER_CLEAR_SESSION = f"X-{flavour}-Clear-Session"

HEADER_ROLE = f"X-{flavour}-Role"
HEADER_SET_ROLE = f"X-{flavour}-Set-Role"

HEADER_STARTED_TRANSACTION = f"X-{flavour}-Started-Transaction-Id"
HEADER_TRANSACTION = f"X-{flavour}-Transaction-Id"

HEADER_PREPARED_STATEMENT = f'X-{flavour}-Prepared-Statement'
HEADER_ADDED_PREPARE = f'X-{flavour}-Added-Prepare'
HEADER_DEALLOCATED_PREPARE = f'X-{flavour}-Deallocated-Prepare'

HEADER_SET_SCHEMA = f"X-{flavour}-Set-Schema"
HEADER_SET_CATALOG = f"X-{flavour}-Set-Catalog"

HEADER_CLIENT_CAPABILITIES = f"X-{flavour}-Client-Capabilities"

LENGTH_TYPES = ["char", "varchar"]
PRECISION_TYPES = ["time", "time with time zone", "timestamp", "timestamp with time zone", "decimal"]
SCALE_TYPES = ["decimal"]
