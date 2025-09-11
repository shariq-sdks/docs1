# API Spec Checker

## Overview

API spec checker compares Java models in authlete-java-common with YAML API spec models defined for
API doc and reports any mismatches. It helps you quickly spot:

- Models present in Java but missing in the YAML spec
- Unknown properties (present in Java, absent in YAML)
- Removed properties (present in YAML, absent in Java)

---

## Command-Line Options

| Flag            | Required | Description                                 | Default | Example                         |
|-----------------|----------|---------------------------------------------|---------| --------------------------------|
| `-ajc-path`     | Yes      | Path to authlete-java-common root directory | N/A     | `/path/to/authlete-java-common` |
| `-api-doc-path` | Yes      | Path to API doc root directory              | N/A     | `/path/to/new-api-doc`          |
| `-server-type`  | Yes      | Server type                                 | N/A     | `shared`                        |
| `-version`      | Yes      | API version                                 | N/A     | `3.0.15`                        |
| `-locale`       | Yes      | Spec locale                                 | N/A     | `en`                            |
| `-format`       | No       | Output format                               | `text`  | `text`                          |

Example:
```bash
go run . \
  -ajc-path /path/to/authlete-java-common \
  -api-doc-path /path/to/new-api-doc \
  -server-type shared \
  -version 3.0.15 \
  -locale en \
  -format text
```

---

## `.metadata.yaml` file

The `.metadata.yaml` file specifies metadata for a target API doc spec.
It must be placed in the target spec directory (e.g. `/shared/3.0.15/en`).

The file defines two top-level properties: `ajcVersion` and `skipRule`.

### 1. `ajcVersion`

Specifies the version of authlete-java-common to compare the target API doc spec against.
This must be set to a string, e.g.:

```
ajcVersion: "4.20"
```

### 2. `skipRule`

The `skipRule` section controls which packages, models, and properties should be ignored during comparison.
It has three subsections:

#### 2.1. `packages`

- A list of fully qualified package names to ignore.
- All models under the listed packages are skipped, and are not treated as unknown.

Example:

```
skipRule:
  packages:
    - com.authlete.common.annotationprocessor
    - com.authlete.common.api
```

#### 2.2. `models`

- A list of fully qualified class (model) names to ignore.
- The listed models are skipped, and are not treated as unknown.

Example:

```
skipRule:
  models:
    - com.authlete.common.dto.ApiResponse
    - com.authlete.common.dto.AuthorizationTicketInfo
```

#### 2.3. `properties`

- A map from a fully qualified class name to a list of properties in that class to ignore.
- The listed properties are skipped, and are not treated as unknown.

Example:

```
skipRule:
  properties:
    com.authlete.common.dto.Service:
      - serviceOwnerNumber
      - apiSecret
```

Here's an example of `.metadata` file.

```
ajcVersion: 4.20
skipRule:
  packages:
    - com.authlete.common.annotationprocessor
    - com.authlete.common.api
    ...
  models:
    - com.authlete.common.dto.ApiResponse
    - com.authlete.common.dto.AuthorizationTicketInfo
    ...
  properties:
    com.authlete.common.dto.Service:
      - serviceOwnerNumber
      - apiSecret
      ...
```

---

## Formatter

The output results can be formatter by a formatter placed under `formatter` directory. (The default
formatter is `text_formatter.go`, which shows results in a human-readable way.)

---

## Example Output

The default formatter `text_formatter.go` results in outputs as follows:

```
[Basic Info]

  API Doc: /path/to/new-api-doc
  API Server Type: shared
  API Version: 3.0.15
  API Locale: en
  Authlete Java Common: /path/to/authlete-java-common

[Model Info]

  Java Package: com.authlete.common.dto
  Java Model Name: CredentialOfferCreateRequest
  Yaml Model Name: vci_offer_create_request

  [Unknown Properties]
    - credentialConfigurationIds
    - txCode
    - txCodeInputMode
    - txCodeDescription

  [Removed Properties]
    - credentials
    - userPinRequired
    - userPinLength
```

---