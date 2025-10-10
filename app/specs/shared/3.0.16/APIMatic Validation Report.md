# <a id="apimatic-validation-report"></a> APIMatic Validation Report

## <a id="introduction"></a> Introduction

The following report is addressed to **mkm**. It was compiled on **October 09, 2025** using APIMatic and contains a validation summary of all API definitions involved.

### <a id="what-is-apimatic"></a> What is APIMatic?

[APIMatic](https://apimatic.io) is a Developer Experience platform for Web APIs, offering auto-generated SDKs, usage examples, and interactive documentation. Our goal is to streamline API onboarding and adoption.

### <a id="api-definition-validation"></a> API Definition Validation

APIMatic ensures API specifications are syntactically and semantically correct to generate high-quality documentation and SDKs. This report details the validation results, highlighting any blockers that must be resolved. Visit our [official documentation](https://docs.apimatic.io/validate-lint-apis/overview/).

### <a id="fixing-validation-issues"></a> Fixing Validation Issues

To resolve issues or re-validate API definitions, use our VS Code extension [**Fix My OpenAPI**](https://www.apimatic.io/solution/fix-my-openapi), which offers dedicated views and other features for improving API definitions.

### <a id="contact-us"></a> Contact Us

For queries or concerns, reach out to us at [support@apimatic.io](mailto:support@apimatic.io).

## Table Of Contents

  * [Data Overview](#data-overview)
  * [Validation Summary](#validation-summary)
  * [Validation Issues (1)](#validation-issues-1)
    * [`Warn` Issue No. 1 - Multiple main API description files detected in the files uploaded. (2)](#warn-issue-no-1---multiple-main-api-description-files-detected-in-the-files-uploaded-2)
  * [Lint Issues (14)](#lint-issues-14)
    * [`Error` Issue No. 1 - Duplicate parameter names found. (1)](#error-issue-no-1---duplicate-parameter-names-found-1)
    * [`Error` Issue No. 2 - The schema `required` list references an undefined schema property. (1)](#error-issue-no-2---the-schema-required-list-references-an-undefined-schema-property-1)
    * [`Error` Issue No. 3 - Operation summary is invalid. (11)](#error-issue-no-3---operation-summary-is-invalid-11)
    * [`Warn` Issue No. 4 - Path may result in ambiguous resolution. (2)](#warn-issue-no-4---path-may-result-in-ambiguous-resolution-2)
    * [`Warn` Issue No. 5 - Inline complex schema definition found. (895)](#warn-issue-no-5---inline-complex-schema-definition-found-895)
    * [`Warn` Issue No. 6 - Inline enum schema definition found. (234)](#warn-issue-no-6---inline-enum-schema-definition-found-234)
    * [`Warn` Issue No. 7 - Schema object description contains leading/trailing white-space characters. (15)](#warn-issue-no-7---schema-object-description-contains-leadingtrailing-white-space-characters-15)
    * [`Warn` Issue No. 8 - Unsupported extension detected. (3)](#warn-issue-no-8---unsupported-extension-detected-3)
    * [`Warn` Issue No. 9 - Component was defined but never used. (3)](#warn-issue-no-9---component-was-defined-but-never-used-3)
    * [`Warn` Issue No. 10 - Undefined tag used in operation object. (3)](#warn-issue-no-10---undefined-tag-used-in-operation-object-3)
    * [`Warn` Issue No. 11 - No security mechanism applied to the API. (1)](#warn-issue-no-11---no-security-mechanism-applied-to-the-api-1)
    * [`Info` Issue No. 12 - The root OpenAPI file name does not follow recommended conventions. (1)](#info-issue-no-12---the-root-openapi-file-name-does-not-follow-recommended-conventions-1)
    * [`Info` Issue No. 13 - Schema object description is missing. (222)](#info-issue-no-13---schema-object-description-is-missing-222)
    * [`Info` Issue No. 14 - Schema object example/default value is missing. (604)](#info-issue-no-14---schema-object-exampledefault-value-is-missing-604)


## <a id="data-overview"></a> Data Overview

This report analyzes an API named `Authlete API Explorer - Test` which is defined using the specification format `OpenAPI v3.1 (YAML)`. The files involved are listed below: 


| # | File Path | File Specification Format |
| - | -------- | ----- |
| 1 | `en_test.yaml` | OpenAPI v3.1 (YAML) _(Main File)_ |
| 2 | `en.yaml` | OpenAPI v3.1 (YAML) |

## <a id="validation-summary"></a> Validation Summary

Provided API files scored `59.5%` (_Good but can be better_). A total of `1998` issues were found during this process affecting `2` out of `2` file(s).

**Validation Status:** `✔ Passed With Warnings`

**Linting Status:** `✘ Failed With Errors`

The table below gives information about how different issues are distributed:
| Property | Value |
| -------- | ----- |
| Blocking Errors | Total `0`, Validation `0`, Lint `0` |
| Errors | Total `13`, Validation `0`, Lint `13` |
| Warnings | Total `1158`, Validation `2`, Lint `1156` |
| Informational Messages | Total `827`, Validation `0`, Lint `827` |
| Must fix vs Recommended to fix | `0.0%` : `100.0%` |
| Standard Non-Compliance | `0.3%` |
| Syntax | `1.3%` |
| Documentation | `41.3%` |
| Code Generation | `0.6%` |
| Other | `57.1%` |

## <a id="validation-issues-1"></a> Validation Issues (1)

A total no. of `1` validation issues were found which are listed below:
* [`Warn` Issue No. 1 - Multiple main API description files detected in the files uploaded. (2)](#warn-issue-no-1---multiple-main-api-description-files-detected-in-the-files-uploaded-2)
### <a id="warn-issue-no-1---multiple-main-api-description-files-detected-in-the-files-uploaded-2"></a> `Warn` Issue No. 1 - Multiple main API description files detected in the files uploaded. (2)

| Property | Value |
| -------- | ----- |
| Rule Id | `single-main-api-description-file` |
| Ruleset Id | `input-file-validation` |
| Type of Issue | Semantic |
| Broad Category of Issue | File I/O Content |

For multi-file upload, the files must consist of a single main API description file only while the rest of the files must be related in some way to this main file e.g. files referenced by the main file. Including multiple main API description files (e.g. multiple OpenAPI files or an OpenAPI file along with a RAML file, etc.) is not allowed. If multiple main files are discovered, only the first will be considered.

#### <a id="tips"></a> Tips

* A main file serves as the entry point. Multiple entry points are therefore not recommended to prevent any issues in the output.
* A main file is recommended to be an API description file like OpenAPI, RAML, etc. If no API description file is found, the first data description format like JSON Data, JSON Schema, etc. will be picked up as the main file.
* Ideally, the main file should be placed in the root folder. No other main files must be present.
* Make sure that there is only one main file in the uploaded files. Remove any extra files and then re-upload.
* Make sure that the file contents are complete as that can hinder correct identification.

#### <a id="for-more-information"></a> For More Information

* https://docs.apimatic.io/manage-apis/create-or-import-api/#supported-input-formats
* https://docs.apimatic.io/api-transformer/overview-transformer/#supported-formats-in-api-transformer

#### <a id="affected-components-2"></a> Affected Components (`2`)

1. **File:** `en.yaml`, **Line No:** `1`, **Line Pos:** `1` - **Line No:** `1`, **Line Pos:** `2`
    * _**Multiple Main Files:**_ en.yaml : OpenAPI v3.1 (YAML), en_test.yaml : OpenAPI v3.1 (YAML)

2. **File:** `en_test.yaml`, **Line No:** `1`, **Line Pos:** `1` - **Line No:** `1`, **Line Pos:** `2`
    * _**Multiple Main Files:**_ en.yaml : OpenAPI v3.1 (YAML), en_test.yaml : OpenAPI v3.1 (YAML)



## <a id="lint-issues-14"></a> Lint Issues (14)

A total no. of `14` lint issues were found which are listed below:
* [`Error` Issue No. 1 - Duplicate parameter names found. (1)](#error-issue-no-1---duplicate-parameter-names-found-1)
* [`Error` Issue No. 2 - The schema `required` list references an undefined schema property. (1)](#error-issue-no-2---the-schema-required-list-references-an-undefined-schema-property-1)
* [`Error` Issue No. 3 - Operation summary is invalid. (11)](#error-issue-no-3---operation-summary-is-invalid-11)
* [`Warn` Issue No. 4 - Path may result in ambiguous resolution. (2)](#warn-issue-no-4---path-may-result-in-ambiguous-resolution-2)
* [`Warn` Issue No. 5 - Inline complex schema definition found. (895)](#warn-issue-no-5---inline-complex-schema-definition-found-895)
* [`Warn` Issue No. 6 - Inline enum schema definition found. (234)](#warn-issue-no-6---inline-enum-schema-definition-found-234)
* [`Warn` Issue No. 7 - Schema object description contains leading/trailing white-space characters. (15)](#warn-issue-no-7---schema-object-description-contains-leadingtrailing-white-space-characters-15)
* [`Warn` Issue No. 8 - Unsupported extension detected. (3)](#warn-issue-no-8---unsupported-extension-detected-3)
* [`Warn` Issue No. 9 - Component was defined but never used. (3)](#warn-issue-no-9---component-was-defined-but-never-used-3)
* [`Warn` Issue No. 10 - Undefined tag used in operation object. (3)](#warn-issue-no-10---undefined-tag-used-in-operation-object-3)
* [`Warn` Issue No. 11 - No security mechanism applied to the API. (1)](#warn-issue-no-11---no-security-mechanism-applied-to-the-api-1)
* [`Info` Issue No. 12 - The root OpenAPI file name does not follow recommended conventions. (1)](#info-issue-no-12---the-root-openapi-file-name-does-not-follow-recommended-conventions-1)
* [`Info` Issue No. 13 - Schema object description is missing. (222)](#info-issue-no-13---schema-object-description-is-missing-222)
* [`Info` Issue No. 14 - Schema object example/default value is missing. (604)](#info-issue-no-14---schema-object-exampledefault-value-is-missing-604)
### <a id="error-issue-no-1---duplicate-parameter-names-found-1"></a> `Error` Issue No. 1 - Duplicate parameter names found. (1)

| Property | Value |
| -------- | ----- |
| Rule Id | `unique-parameter-name` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Parameters |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

Operation level parameter names and requestBody schema property names should be unique. You can use parameter-level `x-unique-name` to provide unique display name to conflicting parameter.

#### <a id="tips-1"></a> Tips

* Use parameter-level `x-unique-name` to provide unique display name.
* Make sure all parameters have unique names.
* If requestBody object exists, make sure no parameter name is equal to any schema property key in the requestBody.

#### <a id="for-more-information-1"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#parameter-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-1"></a> Affected Components (`1`)

1. **File:** `en.yaml`, **Line No:** `20355`, **Line Pos:** `11` - **Line No:** `20355`, **Line Pos:** `12`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > parameters > 1`
    * _**Duplicate Parameter Name:**_ clientId


### <a id="error-issue-no-2---the-schema-required-list-references-an-undefined-schema-property-1"></a> `Error` Issue No. 2 - The schema `required` list references an undefined schema property. (1)

| Property | Value |
| -------- | ----- |
| Rule Id | `pre-defined-required-schema-property` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Schemas |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

The properties listed in the `required` list of a schema must be pre-defined in the schema properties.

#### <a id="tips-2"></a> Tips

* Ensure that all properties listed in the `required` list of the schema are pre-defined in the schema properties.

#### <a id="for-more-information-2"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schema-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-1-1"></a> Affected Components (`1`)

1. **File:** `en.yaml`, **Line No:** `36007`, **Line Pos:** `19` - **Line No:** `36007`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/gm > post > requestBody > content > application/json > schema > required > 0`
    * _**Required Property:**_ token
    * _**Caller Path:**_ -


### <a id="error-issue-no-3---operation-summary-is-invalid-11"></a> `Error` Issue No. 3 - Operation summary is invalid. (11)

| Property | Value |
| -------- | ----- |
| Rule Id | `valid-operation-summary` |
| Ruleset Id | `openapi-v3-codegen-syntax-linting` |
| Type of Issue | Syntax |
| Broad Category of Issue | OpenAPI Operations |
| Possible Impact On Output Of | `Code Generation`, `Developer Experience Portal` |

For successful Code Generation, the operation summary must only use letters, numbers, underscores and dashes. It must not contain any leading/trailing white-space characters.

#### <a id="tips-3"></a> Tips

* Make sure that the summary of the operation does not contain any forbidden characters.
* Use only letters, numbers, underscores and dashes.
* Remove any trailing/leading white-space characters, if present.

#### <a id="for-more-information-3"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#operation-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-11"></a> Affected Components (`11`)

1. **File:** `en.yaml`, **Line No:** `51777`, **Line Pos:** `16` - **Line No:** `51777`, **Line Pos:** `49`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/metadata API

2. **File:** `en.yaml`, **Line No:** `51911`, **Line Pos:** `16` - **Line No:** `51911`, **Line Pos:** `50`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/jwtissuer API

3. **File:** `en.yaml`, **Line No:** `52044`, **Line Pos:** `16` - **Line No:** `52044`, **Line Pos:** `45`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/jwks API

4. **File:** `en.yaml`, **Line No:** `52177`, **Line Pos:** `16` - **Line No:** `52177`, **Line Pos:** `53`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/offer/create API

5. **File:** `en.yaml`, **Line No:** `52692`, **Line Pos:** `16` - **Line No:** `52692`, **Line Pos:** `51`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/offer/info API

6. **File:** `en.yaml`, **Line No:** `52920`, **Line Pos:** `16` - **Line No:** `52920`, **Line Pos:** `53`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/single/parse API

7. **File:** `en.yaml`, **Line No:** `53068`, **Line Pos:** `16` - **Line No:** `53068`, **Line Pos:** `53`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/single/issue API

8. **File:** `en.yaml`, **Line No:** `53213`, **Line Pos:** `16` - **Line No:** `53213`, **Line Pos:** `52`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/batch/parse API

9. **File:** `en.yaml`, **Line No:** `53366`, **Line Pos:** `16` - **Line No:** `53366`, **Line Pos:** `52`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/batch/issue API

10. **File:** `en.yaml`, **Line No:** `53509`, **Line Pos:** `16` - **Line No:** `53509`, **Line Pos:** `55`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/deferred/parse API

11. **File:** `en.yaml`, **Line No:** `53658`, **Line Pos:** `16` - **Line No:** `53658`, **Line Pos:** `55`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > summary`
    * _**Invalid Operation Summary:**_ /api/{serviceId}/vci/deferred/issue API


### <a id="warn-issue-no-4---path-may-result-in-ambiguous-resolution-2"></a> `Warn` Issue No. 4 - Path may result in ambiguous resolution. (2)

| Property | Value |
| -------- | ----- |
| Rule Id | `no-ambiguous-path` |
| Ruleset Id | `openapi-v3-standards-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | Paths |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

Templated paths should not lead to an ambiguous resolution e.g. /{entity}/me and /books/{id} can result in the same path depending upon the values substituted and so are considered ambiguous.

#### <a id="tips-4"></a> Tips

* If you are sure that the ambiguous templated paths are not likely to conflict with each other because of their possible substitution values, you may ignore this warning.
* If one of the ambiguous paths cover all information of the other path as well, consider removing one of the path definitions.

#### <a id="for-more-information-4"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#path-templating-matching
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#paths-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#path-templating-matching
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#paths-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-2-1"></a> Affected Components (`2`)

1. **File:** `en.yaml`, **Line No:** `15032`, **Line Pos:** `3` - **Line No:** `15032`, **Line Pos:** `41`, **Path:** `# > paths`
    * _**Ambiguous Paths:**_ /api/{serviceId}/client/get/{clientId}, /api/{serviceId}/client/get/list

2. **File:** `en.yaml`, **Line No:** `51474`, **Line Pos:** `3` - **Line No:** `51474`, **Line Pos:** `36`, **Path:** `# > paths`
    * _**Ambiguous Paths:**_ /api/{serviceId}/hsk/get/{handle}, /api/{serviceId}/hsk/get/list


### <a id="warn-issue-no-5---inline-complex-schema-definition-found-895"></a> `Warn` Issue No. 5 - Inline complex schema definition found. (895)

| Property | Value |
| -------- | ----- |
| Rule Id | `no-inline-complex-schema-definition` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Schemas |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

A complex schema is one that may use one or more of the following constructs: `allOf`, `anyOf`, `oneOf`, `not`, `properties`. Such schema definitions must be added globally in the components/schemas section with a unique name and then referenced throughout the API document with that name or should define `title` property alongside the `properties` property. Inline definitions of such schemas are not recommended as for auto-generating SDKs/documentation the names of such schemas are deduced from the parent objects in which they are declared inline. The names deduced this way may not be user-friendly and can conflict with other definitions resulting in name duplication. This behavior can affect your output quality.

#### <a id="tips-5"></a> Tips

* Ensure you are not using any of these constructs in your schema if it is an inline schema definition: `allOf`, `anyOf`, `oneOf`, `not`, `properties`.
* Add `title` property alongside the `properties` property in the schema definition.
* Remove the inline schema definition and relocate it to the components/schemas section.
* Define the inline schema globally in the components/schemas section with a unique name. Then reference it using $ref in your current object with a path like '#/components/schemas/<global name>'.
* Ensure that no other inline schemas are defined.
* If you wish to retain the inline schema definition, try adding a `title` property in the Schema Object definition with a unique name to improve output.

#### <a id="for-more-information-5"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schema-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#componentsObject
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-895"></a> Affected Components (`895`)

1. **File:** `en.yaml`, **Line No:** `150`, **Line Pos:** `17` - **Line No:** `150`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema`

2. **File:** `en.yaml`, **Line No:** `183`, **Line Pos:** `23` - **Line No:** `183`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata > items`

3. **File:** `en.yaml`, **Line No:** `562`, **Line Pos:** `23` - **Line No:** `562`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

4. **File:** `en.yaml`, **Line No:** `682`, **Line Pos:** `23` - **Line No:** `682`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

5. **File:** `en.yaml`, **Line No:** `697`, **Line Pos:** `29` - **Line No:** `697`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

6. **File:** `en.yaml`, **Line No:** `709`, **Line Pos:** `29` - **Line No:** `709`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

7. **File:** `en.yaml`, **Line No:** `1123`, **Line Pos:** `23` - **Line No:** `1123`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes > items`

8. **File:** `en.yaml`, **Line No:** `1299`, **Line Pos:** `23` - **Line No:** `1299`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items`

9. **File:** `en.yaml`, **Line No:** `1664`, **Line Pos:** `23` - **Line No:** `1664`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

10. **File:** `en.yaml`, **Line No:** `1807`, **Line Pos:** `21` - **Line No:** `1807`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

11. **File:** `en.yaml`, **Line No:** `1979`, **Line Pos:** `17` - **Line No:** `1979`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 400 > content > application/json > schema`

12. **File:** `en.yaml`, **Line No:** `1995`, **Line Pos:** `17` - **Line No:** `1995`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 401 > content > application/json > schema`

13. **File:** `en.yaml`, **Line No:** `2011`, **Line Pos:** `17` - **Line No:** `2011`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 403 > content > application/json > schema`

14. **File:** `en.yaml`, **Line No:** `2027`, **Line Pos:** `17` - **Line No:** `2027`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 500 > content > application/json > schema`

15. **File:** `en.yaml`, **Line No:** `2097`, **Line Pos:** `17` - **Line No:** `2097`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema`

16. **File:** `en.yaml`, **Line No:** `2120`, **Line Pos:** `23` - **Line No:** `2120`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items`

17. **File:** `en.yaml`, **Line No:** `2153`, **Line Pos:** `29` - **Line No:** `2153`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata > items`

18. **File:** `en.yaml`, **Line No:** `2532`, **Line Pos:** `29` - **Line No:** `2532`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items`

19. **File:** `en.yaml`, **Line No:** `2652`, **Line Pos:** `29` - **Line No:** `2652`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items`

20. **File:** `en.yaml`, **Line No:** `2667`, **Line Pos:** `35` - **Line No:** `2667`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions > items`

21. **File:** `en.yaml`, **Line No:** `2679`, **Line Pos:** `35` - **Line No:** `2679`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes > items`

22. **File:** `en.yaml`, **Line No:** `3093`, **Line Pos:** `29` - **Line No:** `3093`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes > items`

23. **File:** `en.yaml`, **Line No:** `3269`, **Line Pos:** `29` - **Line No:** `3269`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items`

24. **File:** `en.yaml`, **Line No:** `3634`, **Line Pos:** `29` - **Line No:** `3634`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors > items`

25. **File:** `en.yaml`, **Line No:** `3777`, **Line Pos:** `27` - **Line No:** `3777`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata`

26. **File:** `en.yaml`, **Line No:** `3959`, **Line Pos:** `17` - **Line No:** `3959`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 400 > content > application/json > schema`

27. **File:** `en.yaml`, **Line No:** `3975`, **Line Pos:** `17` - **Line No:** `3975`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 401 > content > application/json > schema`

28. **File:** `en.yaml`, **Line No:** `3991`, **Line Pos:** `17` - **Line No:** `3991`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 403 > content > application/json > schema`

29. **File:** `en.yaml`, **Line No:** `4007`, **Line Pos:** `17` - **Line No:** `4007`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 500 > content > application/json > schema`

30. **File:** `en.yaml`, **Line No:** `4056`, **Line Pos:** `15` - **Line No:** `4056`, **Line Pos:** `16`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema`

31. **File:** `en.yaml`, **Line No:** `4089`, **Line Pos:** `21` - **Line No:** `4089`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata > items`

32. **File:** `en.yaml`, **Line No:** `4468`, **Line Pos:** `21` - **Line No:** `4468`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items`

33. **File:** `en.yaml`, **Line No:** `4588`, **Line Pos:** `21` - **Line No:** `4588`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items`

34. **File:** `en.yaml`, **Line No:** `4603`, **Line Pos:** `27` - **Line No:** `4603`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

35. **File:** `en.yaml`, **Line No:** `4615`, **Line Pos:** `27` - **Line No:** `4615`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

36. **File:** `en.yaml`, **Line No:** `5029`, **Line Pos:** `21` - **Line No:** `5029`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > attributes > items`

37. **File:** `en.yaml`, **Line No:** `5205`, **Line Pos:** `21` - **Line No:** `5205`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > hsks > items`

38. **File:** `en.yaml`, **Line No:** `5570`, **Line Pos:** `21` - **Line No:** `5570`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > trustAnchors > items`

39. **File:** `en.yaml`, **Line No:** `5713`, **Line Pos:** `19` - **Line No:** `5713`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata`

40. **File:** `en.yaml`, **Line No:** `5816`, **Line Pos:** `15` - **Line No:** `5816`, **Line Pos:** `16`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema`

41. **File:** `en.yaml`, **Line No:** `5849`, **Line Pos:** `21` - **Line No:** `5849`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > metadata > items`

42. **File:** `en.yaml`, **Line No:** `6228`, **Line Pos:** `21` - **Line No:** `6228`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > mtlsEndpointAliases > items`

43. **File:** `en.yaml`, **Line No:** `6348`, **Line Pos:** `21` - **Line No:** `6348`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items`

44. **File:** `en.yaml`, **Line No:** `6363`, **Line Pos:** `27` - **Line No:** `6363`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > descriptions > items`

45. **File:** `en.yaml`, **Line No:** `6375`, **Line Pos:** `27` - **Line No:** `6375`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > attributes > items`

46. **File:** `en.yaml`, **Line No:** `6789`, **Line Pos:** `21` - **Line No:** `6789`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > attributes > items`

47. **File:** `en.yaml`, **Line No:** `6965`, **Line Pos:** `21` - **Line No:** `6965`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > hsks > items`

48. **File:** `en.yaml`, **Line No:** `7330`, **Line Pos:** `21` - **Line No:** `7330`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > trustAnchors > items`

49. **File:** `en.yaml`, **Line No:** `7473`, **Line Pos:** `19` - **Line No:** `7473`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata`

50. **File:** `en.yaml`, **Line No:** `7545`, **Line Pos:** `17` - **Line No:** `7545`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema`

51. **File:** `en.yaml`, **Line No:** `7578`, **Line Pos:** `23` - **Line No:** `7578`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > metadata > items`

52. **File:** `en.yaml`, **Line No:** `7957`, **Line Pos:** `23` - **Line No:** `7957`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

53. **File:** `en.yaml`, **Line No:** `8077`, **Line Pos:** `23` - **Line No:** `8077`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

54. **File:** `en.yaml`, **Line No:** `8092`, **Line Pos:** `29` - **Line No:** `8092`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

55. **File:** `en.yaml`, **Line No:** `8104`, **Line Pos:** `29` - **Line No:** `8104`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

56. **File:** `en.yaml`, **Line No:** `8518`, **Line Pos:** `23` - **Line No:** `8518`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > attributes > items`

57. **File:** `en.yaml`, **Line No:** `8694`, **Line Pos:** `23` - **Line No:** `8694`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > hsks > items`

58. **File:** `en.yaml`, **Line No:** `9059`, **Line Pos:** `23` - **Line No:** `9059`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

59. **File:** `en.yaml`, **Line No:** `9202`, **Line Pos:** `21` - **Line No:** `9202`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

60. **File:** `en.yaml`, **Line No:** `9365`, **Line Pos:** `17` - **Line No:** `9365`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 400 > content > application/json > schema`

61. **File:** `en.yaml`, **Line No:** `9381`, **Line Pos:** `17` - **Line No:** `9381`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 401 > content > application/json > schema`

62. **File:** `en.yaml`, **Line No:** `9397`, **Line Pos:** `17` - **Line No:** `9397`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 403 > content > application/json > schema`

63. **File:** `en.yaml`, **Line No:** `9413`, **Line Pos:** `17` - **Line No:** `9413`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 500 > content > application/json > schema`

64. **File:** `en.yaml`, **Line No:** `9473`, **Line Pos:** `15` - **Line No:** `9473`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema`

65. **File:** `en.yaml`, **Line No:** `9506`, **Line Pos:** `21` - **Line No:** `9506`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > metadata > items`

66. **File:** `en.yaml`, **Line No:** `9885`, **Line Pos:** `21` - **Line No:** `9885`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items`

67. **File:** `en.yaml`, **Line No:** `10005`, **Line Pos:** `21` - **Line No:** `10005`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedScopes > items`

68. **File:** `en.yaml`, **Line No:** `10020`, **Line Pos:** `27` - **Line No:** `10020`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

69. **File:** `en.yaml`, **Line No:** `10032`, **Line Pos:** `27` - **Line No:** `10032`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

70. **File:** `en.yaml`, **Line No:** `10446`, **Line Pos:** `21` - **Line No:** `10446`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > attributes > items`

71. **File:** `en.yaml`, **Line No:** `10622`, **Line Pos:** `21` - **Line No:** `10622`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > hsks > items`

72. **File:** `en.yaml`, **Line No:** `10987`, **Line Pos:** `21` - **Line No:** `10987`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > trustAnchors > items`

73. **File:** `en.yaml`, **Line No:** `11130`, **Line Pos:** `19` - **Line No:** `11130`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata`

74. **File:** `en.yaml`, **Line No:** `11281`, **Line Pos:** `15` - **Line No:** `11281`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema`

75. **File:** `en.yaml`, **Line No:** `11314`, **Line Pos:** `21` - **Line No:** `11314`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > metadata > items`

76. **File:** `en.yaml`, **Line No:** `11693`, **Line Pos:** `21` - **Line No:** `11693`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > mtlsEndpointAliases > items`

77. **File:** `en.yaml`, **Line No:** `11813`, **Line Pos:** `21` - **Line No:** `11813`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items`

78. **File:** `en.yaml`, **Line No:** `11828`, **Line Pos:** `27` - **Line No:** `11828`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > descriptions > items`

79. **File:** `en.yaml`, **Line No:** `11840`, **Line Pos:** `27` - **Line No:** `11840`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > attributes > items`

80. **File:** `en.yaml`, **Line No:** `12254`, **Line Pos:** `21` - **Line No:** `12254`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > attributes > items`

81. **File:** `en.yaml`, **Line No:** `12430`, **Line Pos:** `21` - **Line No:** `12430`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > hsks > items`

82. **File:** `en.yaml`, **Line No:** `12795`, **Line Pos:** `21` - **Line No:** `12795`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > trustAnchors > items`

83. **File:** `en.yaml`, **Line No:** `12938`, **Line Pos:** `19` - **Line No:** `12938`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata`

84. **File:** `en.yaml`, **Line No:** `13010`, **Line Pos:** `17` - **Line No:** `13010`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema`

85. **File:** `en.yaml`, **Line No:** `13043`, **Line Pos:** `23` - **Line No:** `13043`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > metadata > items`

86. **File:** `en.yaml`, **Line No:** `13422`, **Line Pos:** `23` - **Line No:** `13422`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

87. **File:** `en.yaml`, **Line No:** `13542`, **Line Pos:** `23` - **Line No:** `13542`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

88. **File:** `en.yaml`, **Line No:** `13557`, **Line Pos:** `29` - **Line No:** `13557`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

89. **File:** `en.yaml`, **Line No:** `13569`, **Line Pos:** `29` - **Line No:** `13569`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

90. **File:** `en.yaml`, **Line No:** `13983`, **Line Pos:** `23` - **Line No:** `13983`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > attributes > items`

91. **File:** `en.yaml`, **Line No:** `14159`, **Line Pos:** `23` - **Line No:** `14159`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > hsks > items`

92. **File:** `en.yaml`, **Line No:** `14524`, **Line Pos:** `23` - **Line No:** `14524`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

93. **File:** `en.yaml`, **Line No:** `14667`, **Line Pos:** `21` - **Line No:** `14667`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

94. **File:** `en.yaml`, **Line No:** `14830`, **Line Pos:** `17` - **Line No:** `14830`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 400 > content > application/json > schema`

95. **File:** `en.yaml`, **Line No:** `14846`, **Line Pos:** `17` - **Line No:** `14846`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 401 > content > application/json > schema`

96. **File:** `en.yaml`, **Line No:** `14862`, **Line Pos:** `17` - **Line No:** `14862`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 403 > content > application/json > schema`

97. **File:** `en.yaml`, **Line No:** `14878`, **Line Pos:** `17` - **Line No:** `14878`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 500 > content > application/json > schema`

98. **File:** `en.yaml`, **Line No:** `14947`, **Line Pos:** `17` - **Line No:** `14947`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/delete > delete > responses > 400 > content > application/json > schema`

99. **File:** `en.yaml`, **Line No:** `14963`, **Line Pos:** `17` - **Line No:** `14963`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/delete > delete > responses > 401 > content > application/json > schema`

100. **File:** `en.yaml`, **Line No:** `14979`, **Line Pos:** `17` - **Line No:** `14979`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/delete > delete > responses > 403 > content > application/json > schema`

101. **File:** `en.yaml`, **Line No:** `14995`, **Line Pos:** `17` - **Line No:** `14995`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/delete > delete > responses > 500 > content > application/json > schema`

102. **File:** `en.yaml`, **Line No:** `15056`, **Line Pos:** `17` - **Line No:** `15056`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema`

103. **File:** `en.yaml`, **Line No:** `15079`, **Line Pos:** `23` - **Line No:** `15079`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > clientNames > items`

104. **File:** `en.yaml`, **Line No:** `15096`, **Line Pos:** `23` - **Line No:** `15096`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > descriptions > items`

105. **File:** `en.yaml`, **Line No:** `15162`, **Line Pos:** `23` - **Line No:** `15162`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > logoUris > items`

106. **File:** `en.yaml`, **Line No:** `15787`, **Line Pos:** `23` - **Line No:** `15787`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > tosUris > items`

107. **File:** `en.yaml`, **Line No:** `15810`, **Line Pos:** `23` - **Line No:** `15810`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > policyUris > items`

108. **File:** `en.yaml`, **Line No:** `15831`, **Line Pos:** `23` - **Line No:** `15831`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > clientUris > items`

109. **File:** `en.yaml`, **Line No:** `15895`, **Line Pos:** `23` - **Line No:** `15895`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > attributes > items`

110. **File:** `en.yaml`, **Line No:** `15906`, **Line Pos:** `21` - **Line No:** `15906`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > extension`

111. **File:** `en.yaml`, **Line No:** `16289`, **Line Pos:** `17` - **Line No:** `16289`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 400 > content > application/json > schema`

112. **File:** `en.yaml`, **Line No:** `16305`, **Line Pos:** `17` - **Line No:** `16305`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 401 > content > application/json > schema`

113. **File:** `en.yaml`, **Line No:** `16321`, **Line Pos:** `17` - **Line No:** `16321`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 403 > content > application/json > schema`

114. **File:** `en.yaml`, **Line No:** `16337`, **Line Pos:** `17` - **Line No:** `16337`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 500 > content > application/json > schema`

115. **File:** `en.yaml`, **Line No:** `16420`, **Line Pos:** `17` - **Line No:** `16420`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema`

116. **File:** `en.yaml`, **Line No:** `16441`, **Line Pos:** `23` - **Line No:** `16441`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items`

117. **File:** `en.yaml`, **Line No:** `16464`, **Line Pos:** `29` - **Line No:** `16464`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > clientNames > items`

118. **File:** `en.yaml`, **Line No:** `16481`, **Line Pos:** `29` - **Line No:** `16481`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > descriptions > items`

119. **File:** `en.yaml`, **Line No:** `16547`, **Line Pos:** `29` - **Line No:** `16547`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > logoUris > items`

120. **File:** `en.yaml`, **Line No:** `17172`, **Line Pos:** `29` - **Line No:** `17172`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > tosUris > items`

121. **File:** `en.yaml`, **Line No:** `17195`, **Line Pos:** `29` - **Line No:** `17195`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > policyUris > items`

122. **File:** `en.yaml`, **Line No:** `17216`, **Line Pos:** `29` - **Line No:** `17216`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > clientUris > items`

123. **File:** `en.yaml`, **Line No:** `17280`, **Line Pos:** `29` - **Line No:** `17280`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > attributes > items`

124. **File:** `en.yaml`, **Line No:** `17291`, **Line Pos:** `27` - **Line No:** `17291`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > extension`

125. **File:** `en.yaml`, **Line No:** `17695`, **Line Pos:** `17` - **Line No:** `17695`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 400 > content > application/json > schema`

126. **File:** `en.yaml`, **Line No:** `17711`, **Line Pos:** `17` - **Line No:** `17711`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 401 > content > application/json > schema`

127. **File:** `en.yaml`, **Line No:** `17727`, **Line Pos:** `17` - **Line No:** `17727`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 403 > content > application/json > schema`

128. **File:** `en.yaml`, **Line No:** `17743`, **Line Pos:** `17` - **Line No:** `17743`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 500 > content > application/json > schema`

129. **File:** `en.yaml`, **Line No:** `17801`, **Line Pos:** `15` - **Line No:** `17801`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema`

130. **File:** `en.yaml`, **Line No:** `17824`, **Line Pos:** `21` - **Line No:** `17824`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > clientNames > items`

131. **File:** `en.yaml`, **Line No:** `17841`, **Line Pos:** `21` - **Line No:** `17841`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > descriptions > items`

132. **File:** `en.yaml`, **Line No:** `17907`, **Line Pos:** `21` - **Line No:** `17907`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > logoUris > items`

133. **File:** `en.yaml`, **Line No:** `18532`, **Line Pos:** `21` - **Line No:** `18532`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > tosUris > items`

134. **File:** `en.yaml`, **Line No:** `18555`, **Line Pos:** `21` - **Line No:** `18555`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > policyUris > items`

135. **File:** `en.yaml`, **Line No:** `18576`, **Line Pos:** `21` - **Line No:** `18576`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > clientUris > items`

136. **File:** `en.yaml`, **Line No:** `18640`, **Line Pos:** `21` - **Line No:** `18640`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > attributes > items`

137. **File:** `en.yaml`, **Line No:** `18651`, **Line Pos:** `19` - **Line No:** `18651`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/create > post > requestBody > content > application/json > schema > properties > extension`

138. **File:** `en.yaml`, **Line No:** `19016`, **Line Pos:** `17` - **Line No:** `19016`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema`

139. **File:** `en.yaml`, **Line No:** `19039`, **Line Pos:** `23` - **Line No:** `19039`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > clientNames > items`

140. **File:** `en.yaml`, **Line No:** `19056`, **Line Pos:** `23` - **Line No:** `19056`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > descriptions > items`

141. **File:** `en.yaml`, **Line No:** `19122`, **Line Pos:** `23` - **Line No:** `19122`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > logoUris > items`

142. **File:** `en.yaml`, **Line No:** `19747`, **Line Pos:** `23` - **Line No:** `19747`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > tosUris > items`

143. **File:** `en.yaml`, **Line No:** `19770`, **Line Pos:** `23` - **Line No:** `19770`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > policyUris > items`

144. **File:** `en.yaml`, **Line No:** `19791`, **Line Pos:** `23` - **Line No:** `19791`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > clientUris > items`

145. **File:** `en.yaml`, **Line No:** `19855`, **Line Pos:** `23` - **Line No:** `19855`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > attributes > items`

146. **File:** `en.yaml`, **Line No:** `19866`, **Line Pos:** `21` - **Line No:** `19866`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 200 > content > application/json > schema > properties > extension`

147. **File:** `en.yaml`, **Line No:** `20249`, **Line Pos:** `17` - **Line No:** `20249`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 400 > content > application/json > schema`

148. **File:** `en.yaml`, **Line No:** `20265`, **Line Pos:** `17` - **Line No:** `20265`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 401 > content > application/json > schema`

149. **File:** `en.yaml`, **Line No:** `20281`, **Line Pos:** `17` - **Line No:** `20281`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 403 > content > application/json > schema`

150. **File:** `en.yaml`, **Line No:** `20297`, **Line Pos:** `17` - **Line No:** `20297`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/create > post > responses > 500 > content > application/json > schema`

151. **File:** `en.yaml`, **Line No:** `20365`, **Line Pos:** `15` - **Line No:** `20365`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema`

152. **File:** `en.yaml`, **Line No:** `20388`, **Line Pos:** `21` - **Line No:** `20388`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > clientNames > items`

153. **File:** `en.yaml`, **Line No:** `20405`, **Line Pos:** `21` - **Line No:** `20405`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > descriptions > items`

154. **File:** `en.yaml`, **Line No:** `20471`, **Line Pos:** `21` - **Line No:** `20471`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > logoUris > items`

155. **File:** `en.yaml`, **Line No:** `21096`, **Line Pos:** `21` - **Line No:** `21096`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > tosUris > items`

156. **File:** `en.yaml`, **Line No:** `21119`, **Line Pos:** `21` - **Line No:** `21119`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > policyUris > items`

157. **File:** `en.yaml`, **Line No:** `21140`, **Line Pos:** `21` - **Line No:** `21140`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > clientUris > items`

158. **File:** `en.yaml`, **Line No:** `21204`, **Line Pos:** `21` - **Line No:** `21204`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > attributes > items`

159. **File:** `en.yaml`, **Line No:** `21215`, **Line Pos:** `19` - **Line No:** `21215`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/json > schema > properties > extension`

160. **File:** `en.yaml`, **Line No:** `21589`, **Line Pos:** `15` - **Line No:** `21589`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema`

161. **File:** `en.yaml`, **Line No:** `21612`, **Line Pos:** `21` - **Line No:** `21612`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > clientNames > items`

162. **File:** `en.yaml`, **Line No:** `21629`, **Line Pos:** `21` - **Line No:** `21629`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > descriptions > items`

163. **File:** `en.yaml`, **Line No:** `21695`, **Line Pos:** `21` - **Line No:** `21695`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > logoUris > items`

164. **File:** `en.yaml`, **Line No:** `22320`, **Line Pos:** `21` - **Line No:** `22320`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > tosUris > items`

165. **File:** `en.yaml`, **Line No:** `22343`, **Line Pos:** `21` - **Line No:** `22343`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > policyUris > items`

166. **File:** `en.yaml`, **Line No:** `22364`, **Line Pos:** `21` - **Line No:** `22364`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > clientUris > items`

167. **File:** `en.yaml`, **Line No:** `22428`, **Line Pos:** `21` - **Line No:** `22428`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > attributes > items`

168. **File:** `en.yaml`, **Line No:** `22439`, **Line Pos:** `19` - **Line No:** `22439`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > extension`

169. **File:** `en.yaml`, **Line No:** `22782`, **Line Pos:** `17` - **Line No:** `22782`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema`

170. **File:** `en.yaml`, **Line No:** `22805`, **Line Pos:** `23` - **Line No:** `22805`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > clientNames > items`

171. **File:** `en.yaml`, **Line No:** `22822`, **Line Pos:** `23` - **Line No:** `22822`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > descriptions > items`

172. **File:** `en.yaml`, **Line No:** `22888`, **Line Pos:** `23` - **Line No:** `22888`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > logoUris > items`

173. **File:** `en.yaml`, **Line No:** `23513`, **Line Pos:** `23` - **Line No:** `23513`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > tosUris > items`

174. **File:** `en.yaml`, **Line No:** `23536`, **Line Pos:** `23` - **Line No:** `23536`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > policyUris > items`

175. **File:** `en.yaml`, **Line No:** `23557`, **Line Pos:** `23` - **Line No:** `23557`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > clientUris > items`

176. **File:** `en.yaml`, **Line No:** `23621`, **Line Pos:** `23` - **Line No:** `23621`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > attributes > items`

177. **File:** `en.yaml`, **Line No:** `23632`, **Line Pos:** `21` - **Line No:** `23632`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 200 > content > application/json > schema > properties > extension`

178. **File:** `en.yaml`, **Line No:** `24015`, **Line Pos:** `17` - **Line No:** `24015`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 400 > content > application/json > schema`

179. **File:** `en.yaml`, **Line No:** `24031`, **Line Pos:** `17` - **Line No:** `24031`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 401 > content > application/json > schema`

180. **File:** `en.yaml`, **Line No:** `24047`, **Line Pos:** `17` - **Line No:** `24047`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 403 > content > application/json > schema`

181. **File:** `en.yaml`, **Line No:** `24063`, **Line Pos:** `17` - **Line No:** `24063`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/update/{clientId} > post > responses > 500 > content > application/json > schema`

182. **File:** `en.yaml`, **Line No:** `24138`, **Line Pos:** `17` - **Line No:** `24138`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/delete/{clientId} > delete > responses > 400 > content > application/json > schema`

183. **File:** `en.yaml`, **Line No:** `24154`, **Line Pos:** `17` - **Line No:** `24154`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/delete/{clientId} > delete > responses > 401 > content > application/json > schema`

184. **File:** `en.yaml`, **Line No:** `24170`, **Line Pos:** `17` - **Line No:** `24170`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/delete/{clientId} > delete > responses > 403 > content > application/json > schema`

185. **File:** `en.yaml`, **Line No:** `24186`, **Line Pos:** `17` - **Line No:** `24186`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/delete/{clientId} > delete > responses > 500 > content > application/json > schema`

186. **File:** `en.yaml`, **Line No:** `24246`, **Line Pos:** `15` - **Line No:** `24246`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > requestBody > content > application/json > schema`

187. **File:** `en.yaml`, **Line No:** `24258`, **Line Pos:** `15` - **Line No:** `24258`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > requestBody > content > application/x-www-form-urlencoded > schema`

188. **File:** `en.yaml`, **Line No:** `24272`, **Line Pos:** `17` - **Line No:** `24272`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > responses > 200 > content > application/json > schema`

189. **File:** `en.yaml`, **Line No:** `24288`, **Line Pos:** `17` - **Line No:** `24288`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > responses > 400 > content > application/json > schema`

190. **File:** `en.yaml`, **Line No:** `24304`, **Line Pos:** `17` - **Line No:** `24304`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > responses > 401 > content > application/json > schema`

191. **File:** `en.yaml`, **Line No:** `24320`, **Line Pos:** `17` - **Line No:** `24320`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > responses > 403 > content > application/json > schema`

192. **File:** `en.yaml`, **Line No:** `24336`, **Line Pos:** `17` - **Line No:** `24336`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/lock_flag/update/{clientIdentifier} > post > responses > 500 > content > application/json > schema`

193. **File:** `en.yaml`, **Line No:** `24378`, **Line Pos:** `17` - **Line No:** `24378`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/refresh/{clientIdentifier} > get > responses > 200 > content > application/json > schema`

194. **File:** `en.yaml`, **Line No:** `24404`, **Line Pos:** `17` - **Line No:** `24404`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/refresh/{clientIdentifier} > get > responses > 400 > content > application/json > schema`

195. **File:** `en.yaml`, **Line No:** `24420`, **Line Pos:** `17` - **Line No:** `24420`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/refresh/{clientIdentifier} > get > responses > 401 > content > application/json > schema`

196. **File:** `en.yaml`, **Line No:** `24436`, **Line Pos:** `17` - **Line No:** `24436`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/refresh/{clientIdentifier} > get > responses > 403 > content > application/json > schema`

197. **File:** `en.yaml`, **Line No:** `24452`, **Line Pos:** `17` - **Line No:** `24452`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/refresh/{clientIdentifier} > get > responses > 500 > content > application/json > schema`

198. **File:** `en.yaml`, **Line No:** `24516`, **Line Pos:** `15` - **Line No:** `24516`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > requestBody > content > application/json > schema`

199. **File:** `en.yaml`, **Line No:** `24529`, **Line Pos:** `15` - **Line No:** `24529`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > requestBody > content > application/x-www-form-urlencoded > schema`

200. **File:** `en.yaml`, **Line No:** `24544`, **Line Pos:** `17` - **Line No:** `24544`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > responses > 200 > content > application/json > schema`

201. **File:** `en.yaml`, **Line No:** `24570`, **Line Pos:** `17` - **Line No:** `24570`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > responses > 400 > content > application/json > schema`

202. **File:** `en.yaml`, **Line No:** `24586`, **Line Pos:** `17` - **Line No:** `24586`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > responses > 401 > content > application/json > schema`

203. **File:** `en.yaml`, **Line No:** `24602`, **Line Pos:** `17` - **Line No:** `24602`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > responses > 403 > content > application/json > schema`

204. **File:** `en.yaml`, **Line No:** `24618`, **Line Pos:** `17` - **Line No:** `24618`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/secret/update/{clientIdentifier} > post > responses > 500 > content > application/json > schema`

205. **File:** `en.yaml`, **Line No:** `24715`, **Line Pos:** `17` - **Line No:** `24715`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 200 > content > application/json > schema`

206. **File:** `en.yaml`, **Line No:** `24743`, **Line Pos:** `23` - **Line No:** `24743`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 200 > content > application/json > schema > properties > clients > items`

207. **File:** `en.yaml`, **Line No:** `24759`, **Line Pos:** `29` - **Line No:** `24759`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > clientNames > items`

208. **File:** `en.yaml`, **Line No:** `24776`, **Line Pos:** `29` - **Line No:** `24776`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > descriptions > items`

209. **File:** `en.yaml`, **Line No:** `24827`, **Line Pos:** `17` - **Line No:** `24827`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 400 > content > application/json > schema`

210. **File:** `en.yaml`, **Line No:** `24843`, **Line Pos:** `17` - **Line No:** `24843`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 401 > content > application/json > schema`

211. **File:** `en.yaml`, **Line No:** `24859`, **Line Pos:** `17` - **Line No:** `24859`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 403 > content > application/json > schema`

212. **File:** `en.yaml`, **Line No:** `24875`, **Line Pos:** `17` - **Line No:** `24875`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/get/list/{subject} > get > responses > 500 > content > application/json > schema`

213. **File:** `en.yaml`, **Line No:** `24942`, **Line Pos:** `15` - **Line No:** `24942`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > requestBody > content > application/json > schema`

214. **File:** `en.yaml`, **Line No:** `24966`, **Line Pos:** `15` - **Line No:** `24966`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > requestBody > content > application/x-www-form-urlencoded > schema`

215. **File:** `en.yaml`, **Line No:** `24990`, **Line Pos:** `17` - **Line No:** `24990`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > responses > 200 > content > application/json > schema`

216. **File:** `en.yaml`, **Line No:** `25006`, **Line Pos:** `17` - **Line No:** `25006`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > responses > 400 > content > application/json > schema`

217. **File:** `en.yaml`, **Line No:** `25022`, **Line Pos:** `17` - **Line No:** `25022`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > responses > 401 > content > application/json > schema`

218. **File:** `en.yaml`, **Line No:** `25038`, **Line Pos:** `17` - **Line No:** `25038`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > responses > 403 > content > application/json > schema`

219. **File:** `en.yaml`, **Line No:** `25054`, **Line Pos:** `17` - **Line No:** `25054`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/update/{clientId} > post > responses > 500 > content > application/json > schema`

220. **File:** `en.yaml`, **Line No:** `25142`, **Line Pos:** `17` - **Line No:** `25142`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/delete/{clientId}/{subject} > delete > responses > 200 > content > application/json > schema`

221. **File:** `en.yaml`, **Line No:** `25193`, **Line Pos:** `17` - **Line No:** `25193`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/delete/{clientId}/{subject} > delete > responses > 400 > content > application/json > schema`

222. **File:** `en.yaml`, **Line No:** `25209`, **Line Pos:** `17` - **Line No:** `25209`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/delete/{clientId}/{subject} > delete > responses > 401 > content > application/json > schema`

223. **File:** `en.yaml`, **Line No:** `25225`, **Line Pos:** `17` - **Line No:** `25225`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/delete/{clientId}/{subject} > delete > responses > 403 > content > application/json > schema`

224. **File:** `en.yaml`, **Line No:** `25241`, **Line Pos:** `17` - **Line No:** `25241`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/authorization/delete/{clientId}/{subject} > delete > responses > 500 > content > application/json > schema`

225. **File:** `en.yaml`, **Line No:** `25344`, **Line Pos:** `17` - **Line No:** `25344`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/get/{clientId}/{subject} > get > responses > 200 > content > application/json > schema`

226. **File:** `en.yaml`, **Line No:** `25402`, **Line Pos:** `17` - **Line No:** `25402`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/get/{clientId}/{subject} > get > responses > 400 > content > application/json > schema`

227. **File:** `en.yaml`, **Line No:** `25418`, **Line Pos:** `17` - **Line No:** `25418`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/get/{clientId}/{subject} > get > responses > 401 > content > application/json > schema`

228. **File:** `en.yaml`, **Line No:** `25434`, **Line Pos:** `17` - **Line No:** `25434`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/get/{clientId}/{subject} > get > responses > 403 > content > application/json > schema`

229. **File:** `en.yaml`, **Line No:** `25450`, **Line Pos:** `17` - **Line No:** `25450`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/get/{clientId}/{subject} > get > responses > 500 > content > application/json > schema`

230. **File:** `en.yaml`, **Line No:** `25538`, **Line Pos:** `17` - **Line No:** `25538`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/delete/{clientId}/{subject} > delete > responses > 200 > content > application/json > schema`

231. **File:** `en.yaml`, **Line No:** `25551`, **Line Pos:** `17` - **Line No:** `25551`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/delete/{clientId}/{subject} > delete > responses > 400 > content > application/json > schema`

232. **File:** `en.yaml`, **Line No:** `25567`, **Line Pos:** `17` - **Line No:** `25567`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/delete/{clientId}/{subject} > delete > responses > 401 > content > application/json > schema`

233. **File:** `en.yaml`, **Line No:** `25583`, **Line Pos:** `17` - **Line No:** `25583`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/delete/{clientId}/{subject} > delete > responses > 403 > content > application/json > schema`

234. **File:** `en.yaml`, **Line No:** `25599`, **Line Pos:** `17` - **Line No:** `25599`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/granted_scopes/delete/{clientId}/{subject} > delete > responses > 500 > content > application/json > schema`

235. **File:** `en.yaml`, **Line No:** `26190`, **Line Pos:** `15` - **Line No:** `26190`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > requestBody > content > application/json > schema`

236. **File:** `en.yaml`, **Line No:** `26217`, **Line Pos:** `15` - **Line No:** `26217`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > requestBody > content > application/x-www-form-urlencoded > schema`

237. **File:** `en.yaml`, **Line No:** `26246`, **Line Pos:** `17` - **Line No:** `26246`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema`

238. **File:** `en.yaml`, **Line No:** `26265`, **Line Pos:** `21` - **Line No:** `26265`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > client`

239. **File:** `en.yaml`, **Line No:** `26281`, **Line Pos:** `27` - **Line No:** `26281`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

240. **File:** `en.yaml`, **Line No:** `26298`, **Line Pos:** `27` - **Line No:** `26298`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

241. **File:** `en.yaml`, **Line No:** `26340`, **Line Pos:** `27` - **Line No:** `26340`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > client > properties > logoUris > items`

242. **File:** `en.yaml`, **Line No:** `26361`, **Line Pos:** `27` - **Line No:** `26361`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > client > properties > tosUris > items`

243. **File:** `en.yaml`, **Line No:** `26384`, **Line Pos:** `27` - **Line No:** `26384`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > client > properties > policyUris > items`

244. **File:** `en.yaml`, **Line No:** `26423`, **Line Pos:** `21` - **Line No:** `26423`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service`

245. **File:** `en.yaml`, **Line No:** `26456`, **Line Pos:** `27` - **Line No:** `26456`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > metadata > items`

246. **File:** `en.yaml`, **Line No:** `26835`, **Line Pos:** `27` - **Line No:** `26835`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > mtlsEndpointAliases > items`

247. **File:** `en.yaml`, **Line No:** `26955`, **Line Pos:** `27` - **Line No:** `26955`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > supportedScopes > items`

248. **File:** `en.yaml`, **Line No:** `26970`, **Line Pos:** `33` - **Line No:** `26970`, **Line Pos:** `34`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > supportedScopes > items > properties > descriptions > items`

249. **File:** `en.yaml`, **Line No:** `26982`, **Line Pos:** `33` - **Line No:** `26982`, **Line Pos:** `34`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > supportedScopes > items > properties > attributes > items`

250. **File:** `en.yaml`, **Line No:** `27396`, **Line Pos:** `27` - **Line No:** `27396`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > attributes > items`

251. **File:** `en.yaml`, **Line No:** `27572`, **Line Pos:** `27` - **Line No:** `27572`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > hsks > items`

252. **File:** `en.yaml`, **Line No:** `27937`, **Line Pos:** `27` - **Line No:** `27937`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > trustAnchors > items`

253. **File:** `en.yaml`, **Line No:** `28080`, **Line Pos:** `25` - **Line No:** `28080`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > service > properties > credentialIssuerMetadata`

254. **File:** `en.yaml`, **Line No:** `28149`, **Line Pos:** `23` - **Line No:** `28149`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > scopes > items`

255. **File:** `en.yaml`, **Line No:** `28164`, **Line Pos:** `29` - **Line No:** `28164`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > descriptions > items`

256. **File:** `en.yaml`, **Line No:** `28176`, **Line Pos:** `29` - **Line No:** `28176`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > attributes > items`

257. **File:** `en.yaml`, **Line No:** `28407`, **Line Pos:** `21` - **Line No:** `28407`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

258. **File:** `en.yaml`, **Line No:** `28416`, **Line Pos:** `27` - **Line No:** `28416`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

259. **File:** `en.yaml`, **Line No:** `28506`, **Line Pos:** `23` - **Line No:** `28506`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > dynamicScopes > items`

260. **File:** `en.yaml`, **Line No:** `28538`, **Line Pos:** `21` - **Line No:** `28538`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > grant`

261. **File:** `en.yaml`, **Line No:** `28543`, **Line Pos:** `27` - **Line No:** `28543`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > grant > properties > scopes > items`

262. **File:** `en.yaml`, **Line No:** `28562`, **Line Pos:** `25` - **Line No:** `28562`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails`

263. **File:** `en.yaml`, **Line No:** `28571`, **Line Pos:** `31` - **Line No:** `28571`, **Line Pos:** `32`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails > properties > elements > items`

264. **File:** `en.yaml`, **Line No:** `28764`, **Line Pos:** `21` - **Line No:** `28764`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > credentialOfferInfo`

265. **File:** `en.yaml`, **Line No:** `28816`, **Line Pos:** `27` - **Line No:** `28816`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 200 > content > application/json > schema > properties > credentialOfferInfo > properties > properties > items`

266. **File:** `en.yaml`, **Line No:** `28925`, **Line Pos:** `17` - **Line No:** `28925`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 400 > content > application/json > schema`

267. **File:** `en.yaml`, **Line No:** `28941`, **Line Pos:** `17` - **Line No:** `28941`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 401 > content > application/json > schema`

268. **File:** `en.yaml`, **Line No:** `28957`, **Line Pos:** `17` - **Line No:** `28957`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 403 > content > application/json > schema`

269. **File:** `en.yaml`, **Line No:** `28973`, **Line Pos:** `17` - **Line No:** `28973`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization > post > responses > 500 > content > application/json > schema`

270. **File:** `en.yaml`, **Line No:** `29143`, **Line Pos:** `15` - **Line No:** `29143`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > requestBody > content > application/json > schema`

271. **File:** `en.yaml`, **Line No:** `29180`, **Line Pos:** `15` - **Line No:** `29180`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > requestBody > content > application/x-www-form-urlencoded > schema`

272. **File:** `en.yaml`, **Line No:** `29218`, **Line Pos:** `17` - **Line No:** `29218`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > responses > 200 > content > application/json > schema`

273. **File:** `en.yaml`, **Line No:** `29249`, **Line Pos:** `17` - **Line No:** `29249`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > responses > 400 > content > application/json > schema`

274. **File:** `en.yaml`, **Line No:** `29265`, **Line Pos:** `17` - **Line No:** `29265`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > responses > 401 > content > application/json > schema`

275. **File:** `en.yaml`, **Line No:** `29281`, **Line Pos:** `17` - **Line No:** `29281`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > responses > 403 > content > application/json > schema`

276. **File:** `en.yaml`, **Line No:** `29297`, **Line Pos:** `17` - **Line No:** `29297`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/fail > post > responses > 500 > content > application/json > schema`

277. **File:** `en.yaml`, **Line No:** `29472`, **Line Pos:** `15` - **Line No:** `29472`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/json > schema`

278. **File:** `en.yaml`, **Line No:** `29501`, **Line Pos:** `21` - **Line No:** `29501`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/json > schema > properties > properties > items`

279. **File:** `en.yaml`, **Line No:** `29544`, **Line Pos:** `19` - **Line No:** `29544`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/json > schema > properties > authorizationDetails`

280. **File:** `en.yaml`, **Line No:** `29553`, **Line Pos:** `25` - **Line No:** `29553`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

281. **File:** `en.yaml`, **Line No:** `29731`, **Line Pos:** `15` - **Line No:** `29731`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/x-www-form-urlencoded > schema`

282. **File:** `en.yaml`, **Line No:** `29760`, **Line Pos:** `21` - **Line No:** `29760`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

283. **File:** `en.yaml`, **Line No:** `29803`, **Line Pos:** `19` - **Line No:** `29803`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorizationDetails`

284. **File:** `en.yaml`, **Line No:** `29812`, **Line Pos:** `25` - **Line No:** `29812`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorizationDetails > properties > elements > items`

285. **File:** `en.yaml`, **Line No:** `29991`, **Line Pos:** `17` - **Line No:** `29991`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > responses > 200 > content > application/json > schema`

286. **File:** `en.yaml`, **Line No:** `30060`, **Line Pos:** `17` - **Line No:** `30060`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > responses > 400 > content > application/json > schema`

287. **File:** `en.yaml`, **Line No:** `30076`, **Line Pos:** `17` - **Line No:** `30076`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > responses > 401 > content > application/json > schema`

288. **File:** `en.yaml`, **Line No:** `30092`, **Line Pos:** `17` - **Line No:** `30092`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > responses > 403 > content > application/json > schema`

289. **File:** `en.yaml`, **Line No:** `30108`, **Line Pos:** `17` - **Line No:** `30108`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/issue > post > responses > 500 > content > application/json > schema`

290. **File:** `en.yaml`, **Line No:** `30168`, **Line Pos:** `15` - **Line No:** `30168`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > requestBody > content > application/json > schema`

291. **File:** `en.yaml`, **Line No:** `30229`, **Line Pos:** `15` - **Line No:** `30229`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > requestBody > content > application/x-www-form-urlencoded > schema`

292. **File:** `en.yaml`, **Line No:** `30294`, **Line Pos:** `17` - **Line No:** `30294`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > responses > 200 > content > application/json > schema`

293. **File:** `en.yaml`, **Line No:** `30351`, **Line Pos:** `17` - **Line No:** `30351`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > responses > 400 > content > application/json > schema`

294. **File:** `en.yaml`, **Line No:** `30367`, **Line Pos:** `17` - **Line No:** `30367`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > responses > 401 > content > application/json > schema`

295. **File:** `en.yaml`, **Line No:** `30383`, **Line Pos:** `17` - **Line No:** `30383`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > responses > 403 > content > application/json > schema`

296. **File:** `en.yaml`, **Line No:** `30399`, **Line Pos:** `17` - **Line No:** `30399`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/pushed_auth_req > post > responses > 500 > content > application/json > schema`

297. **File:** `en.yaml`, **Line No:** `30903`, **Line Pos:** `15` - **Line No:** `30903`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > requestBody > content > application/json > schema`

298. **File:** `en.yaml`, **Line No:** `31016`, **Line Pos:** `15` - **Line No:** `31016`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > requestBody > content > application/x-www-form-urlencoded > schema`

299. **File:** `en.yaml`, **Line No:** `31129`, **Line Pos:** `17` - **Line No:** `31129`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema`

300. **File:** `en.yaml`, **Line No:** `31238`, **Line Pos:** `23` - **Line No:** `31238`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > properties > items`

301. **File:** `en.yaml`, **Line No:** `31275`, **Line Pos:** `21` - **Line No:** `31275`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

302. **File:** `en.yaml`, **Line No:** `31284`, **Line Pos:** `27` - **Line No:** `31284`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

303. **File:** `en.yaml`, **Line No:** `31355`, **Line Pos:** `23` - **Line No:** `31355`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

304. **File:** `en.yaml`, **Line No:** `31368`, **Line Pos:** `23` - **Line No:** `31368`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

305. **File:** `en.yaml`, **Line No:** `31427`, **Line Pos:** `21` - **Line No:** `31427`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > subjectTokenInfo`

306. **File:** `en.yaml`, **Line No:** `31453`, **Line Pos:** `27` - **Line No:** `31453`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > subjectTokenInfo > properties > properties > items`

307. **File:** `en.yaml`, **Line No:** `31472`, **Line Pos:** `25` - **Line No:** `31472`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > subjectTokenInfo > properties > authorizationDetails`

308. **File:** `en.yaml`, **Line No:** `31563`, **Line Pos:** `21` - **Line No:** `31563`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > actorTokenInfo`

309. **File:** `en.yaml`, **Line No:** `31589`, **Line Pos:** `27` - **Line No:** `31589`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > actorTokenInfo > properties > properties > items`

310. **File:** `en.yaml`, **Line No:** `31608`, **Line Pos:** `25` - **Line No:** `31608`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 200 > content > application/json > schema > properties > actorTokenInfo > properties > authorizationDetails`

311. **File:** `en.yaml`, **Line No:** `31795`, **Line Pos:** `17` - **Line No:** `31795`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 400 > content > application/json > schema`

312. **File:** `en.yaml`, **Line No:** `31811`, **Line Pos:** `17` - **Line No:** `31811`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 401 > content > application/json > schema`

313. **File:** `en.yaml`, **Line No:** `31827`, **Line Pos:** `17` - **Line No:** `31827`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 403 > content > application/json > schema`

314. **File:** `en.yaml`, **Line No:** `31843`, **Line Pos:** `17` - **Line No:** `31843`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token > post > responses > 500 > content > application/json > schema`

315. **File:** `en.yaml`, **Line No:** `31973`, **Line Pos:** `15` - **Line No:** `31973`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > requestBody > content > application/json > schema`

316. **File:** `en.yaml`, **Line No:** `31995`, **Line Pos:** `15` - **Line No:** `31995`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > requestBody > content > application/x-www-form-urlencoded > schema`

317. **File:** `en.yaml`, **Line No:** `32018`, **Line Pos:** `17` - **Line No:** `32018`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > responses > 200 > content > application/json > schema`

318. **File:** `en.yaml`, **Line No:** `32047`, **Line Pos:** `17` - **Line No:** `32047`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > responses > 400 > content > application/json > schema`

319. **File:** `en.yaml`, **Line No:** `32063`, **Line Pos:** `17` - **Line No:** `32063`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > responses > 401 > content > application/json > schema`

320. **File:** `en.yaml`, **Line No:** `32079`, **Line Pos:** `17` - **Line No:** `32079`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > responses > 403 > content > application/json > schema`

321. **File:** `en.yaml`, **Line No:** `32095`, **Line Pos:** `17` - **Line No:** `32095`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/fail > post > responses > 500 > content > application/json > schema`

322. **File:** `en.yaml`, **Line No:** `32223`, **Line Pos:** `15` - **Line No:** `32223`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > requestBody > content > application/json > schema`

323. **File:** `en.yaml`, **Line No:** `32239`, **Line Pos:** `21` - **Line No:** `32239`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > requestBody > content > application/json > schema > properties > properties > items`

324. **File:** `en.yaml`, **Line No:** `32287`, **Line Pos:** `15` - **Line No:** `32287`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > requestBody > content > application/x-www-form-urlencoded > schema`

325. **File:** `en.yaml`, **Line No:** `32303`, **Line Pos:** `21` - **Line No:** `32303`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

326. **File:** `en.yaml`, **Line No:** `32352`, **Line Pos:** `17` - **Line No:** `32352`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 200 > content > application/json > schema`

327. **File:** `en.yaml`, **Line No:** `32428`, **Line Pos:** `23` - **Line No:** `32428`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 200 > content > application/json > schema > properties > properties > items`

328. **File:** `en.yaml`, **Line No:** `32457`, **Line Pos:** `21` - **Line No:** `32457`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

329. **File:** `en.yaml`, **Line No:** `32466`, **Line Pos:** `27` - **Line No:** `32466`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

330. **File:** `en.yaml`, **Line No:** `32537`, **Line Pos:** `23` - **Line No:** `32537`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

331. **File:** `en.yaml`, **Line No:** `32550`, **Line Pos:** `23` - **Line No:** `32550`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

332. **File:** `en.yaml`, **Line No:** `32604`, **Line Pos:** `17` - **Line No:** `32604`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 400 > content > application/json > schema`

333. **File:** `en.yaml`, **Line No:** `32620`, **Line Pos:** `17` - **Line No:** `32620`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 401 > content > application/json > schema`

334. **File:** `en.yaml`, **Line No:** `32636`, **Line Pos:** `17` - **Line No:** `32636`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 403 > content > application/json > schema`

335. **File:** `en.yaml`, **Line No:** `32652`, **Line Pos:** `17` - **Line No:** `32652`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/issue > post > responses > 500 > content > application/json > schema`

336. **File:** `en.yaml`, **Line No:** `32874`, **Line Pos:** `15` - **Line No:** `32874`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > requestBody > content > application/json > schema`

337. **File:** `en.yaml`, **Line No:** `32964`, **Line Pos:** `21` - **Line No:** `32964`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > requestBody > content > application/json > schema > properties > headers > items`

338. **File:** `en.yaml`, **Line No:** `33024`, **Line Pos:** `15` - **Line No:** `33024`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > requestBody > content > application/x-www-form-urlencoded > schema`

339. **File:** `en.yaml`, **Line No:** `33114`, **Line Pos:** `21` - **Line No:** `33114`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > headers > items`

340. **File:** `en.yaml`, **Line No:** `33172`, **Line Pos:** `17` - **Line No:** `33172`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema`

341. **File:** `en.yaml`, **Line No:** `33245`, **Line Pos:** `23` - **Line No:** `33245`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > properties > items`

342. **File:** `en.yaml`, **Line No:** `33288`, **Line Pos:** `21` - **Line No:** `33288`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

343. **File:** `en.yaml`, **Line No:** `33297`, **Line Pos:** `27` - **Line No:** `33297`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

344. **File:** `en.yaml`, **Line No:** `33368`, **Line Pos:** `23` - **Line No:** `33368`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

345. **File:** `en.yaml`, **Line No:** `33381`, **Line Pos:** `23` - **Line No:** `33381`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

346. **File:** `en.yaml`, **Line No:** `33394`, **Line Pos:** `23` - **Line No:** `33394`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > scopeDetails > items`

347. **File:** `en.yaml`, **Line No:** `33409`, **Line Pos:** `29` - **Line No:** `33409`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > scopeDetails > items > properties > descriptions > items`

348. **File:** `en.yaml`, **Line No:** `33421`, **Line Pos:** `29` - **Line No:** `33421`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > scopeDetails > items > properties > attributes > items`

349. **File:** `en.yaml`, **Line No:** `33442`, **Line Pos:** `21` - **Line No:** `33442`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > grant`

350. **File:** `en.yaml`, **Line No:** `33447`, **Line Pos:** `27` - **Line No:** `33447`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > grant > properties > scopes > items`

351. **File:** `en.yaml`, **Line No:** `33466`, **Line Pos:** `25` - **Line No:** `33466`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails`

352. **File:** `en.yaml`, **Line No:** `33475`, **Line Pos:** `31` - **Line No:** `33475`, **Line Pos:** `32`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails > properties > elements > items`

353. **File:** `en.yaml`, **Line No:** `33646`, **Line Pos:** `17` - **Line No:** `33646`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 400 > content > application/json > schema`

354. **File:** `en.yaml`, **Line No:** `33662`, **Line Pos:** `17` - **Line No:** `33662`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 401 > content > application/json > schema`

355. **File:** `en.yaml`, **Line No:** `33678`, **Line Pos:** `17` - **Line No:** `33678`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 403 > content > application/json > schema`

356. **File:** `en.yaml`, **Line No:** `33694`, **Line Pos:** `17` - **Line No:** `33694`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection > post > responses > 500 > content > application/json > schema`

357. **File:** `en.yaml`, **Line No:** `33848`, **Line Pos:** `15` - **Line No:** `33848`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > requestBody > content > application/json > schema`

358. **File:** `en.yaml`, **Line No:** `33946`, **Line Pos:** `15` - **Line No:** `33946`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > requestBody > content > application/x-www-form-urlencoded > schema`

359. **File:** `en.yaml`, **Line No:** `34046`, **Line Pos:** `17` - **Line No:** `34046`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > responses > 200 > content > application/json > schema`

360. **File:** `en.yaml`, **Line No:** `34076`, **Line Pos:** `17` - **Line No:** `34076`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > responses > 400 > content > application/json > schema`

361. **File:** `en.yaml`, **Line No:** `34092`, **Line Pos:** `17` - **Line No:** `34092`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > responses > 401 > content > application/json > schema`

362. **File:** `en.yaml`, **Line No:** `34108`, **Line Pos:** `17` - **Line No:** `34108`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > responses > 403 > content > application/json > schema`

363. **File:** `en.yaml`, **Line No:** `34124`, **Line Pos:** `17` - **Line No:** `34124`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/introspection/standard > post > responses > 500 > content > application/json > schema`

364. **File:** `en.yaml`, **Line No:** `34313`, **Line Pos:** `15` - **Line No:** `34313`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > requestBody > content > application/json > schema`

365. **File:** `en.yaml`, **Line No:** `34366`, **Line Pos:** `15` - **Line No:** `34366`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > requestBody > content > application/x-www-form-urlencoded > schema`

366. **File:** `en.yaml`, **Line No:** `34419`, **Line Pos:** `17` - **Line No:** `34419`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > responses > 200 > content > application/json > schema`

367. **File:** `en.yaml`, **Line No:** `34449`, **Line Pos:** `17` - **Line No:** `34449`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > responses > 400 > content > application/json > schema`

368. **File:** `en.yaml`, **Line No:** `34465`, **Line Pos:** `17` - **Line No:** `34465`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > responses > 401 > content > application/json > schema`

369. **File:** `en.yaml`, **Line No:** `34481`, **Line Pos:** `17` - **Line No:** `34481`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > responses > 403 > content > application/json > schema`

370. **File:** `en.yaml`, **Line No:** `34497`, **Line Pos:** `17` - **Line No:** `34497`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/revocation > post > responses > 500 > content > application/json > schema`

371. **File:** `en.yaml`, **Line No:** `34695`, **Line Pos:** `15` - **Line No:** `34695`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > requestBody > content > application/json > schema`

372. **File:** `en.yaml`, **Line No:** `34743`, **Line Pos:** `21` - **Line No:** `34743`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > requestBody > content > application/json > schema > properties > headers > items`

373. **File:** `en.yaml`, **Line No:** `34800`, **Line Pos:** `15` - **Line No:** `34800`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > requestBody > content > application/x-www-form-urlencoded > schema`

374. **File:** `en.yaml`, **Line No:** `34848`, **Line Pos:** `21` - **Line No:** `34848`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > headers > items`

375. **File:** `en.yaml`, **Line No:** `34907`, **Line Pos:** `17` - **Line No:** `34907`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 200 > content > application/json > schema`

376. **File:** `en.yaml`, **Line No:** `34966`, **Line Pos:** `23` - **Line No:** `34966`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 200 > content > application/json > schema > properties > properties > items`

377. **File:** `en.yaml`, **Line No:** `35031`, **Line Pos:** `23` - **Line No:** `35031`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

378. **File:** `en.yaml`, **Line No:** `35044`, **Line Pos:** `23` - **Line No:** `35044`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

379. **File:** `en.yaml`, **Line No:** `35177`, **Line Pos:** `17` - **Line No:** `35177`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 400 > content > application/json > schema`

380. **File:** `en.yaml`, **Line No:** `35193`, **Line Pos:** `17` - **Line No:** `35193`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 401 > content > application/json > schema`

381. **File:** `en.yaml`, **Line No:** `35209`, **Line Pos:** `17` - **Line No:** `35209`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 403 > content > application/json > schema`

382. **File:** `en.yaml`, **Line No:** `35225`, **Line Pos:** `17` - **Line No:** `35225`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo > post > responses > 500 > content > application/json > schema`

383. **File:** `en.yaml`, **Line No:** `35431`, **Line Pos:** `15` - **Line No:** `35431`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > requestBody > content > application/json > schema`

384. **File:** `en.yaml`, **Line No:** `35460`, **Line Pos:** `21` - **Line No:** `35460`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > requestBody > content > application/json > schema > properties > headers > items`

385. **File:** `en.yaml`, **Line No:** `35539`, **Line Pos:** `15` - **Line No:** `35539`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > requestBody > content > application/x-www-form-urlencoded > schema`

386. **File:** `en.yaml`, **Line No:** `35568`, **Line Pos:** `21` - **Line No:** `35568`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > headers > items`

387. **File:** `en.yaml`, **Line No:** `35649`, **Line Pos:** `17` - **Line No:** `35649`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > responses > 200 > content > application/json > schema`

388. **File:** `en.yaml`, **Line No:** `35694`, **Line Pos:** `17` - **Line No:** `35694`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > responses > 400 > content > application/json > schema`

389. **File:** `en.yaml`, **Line No:** `35710`, **Line Pos:** `17` - **Line No:** `35710`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > responses > 401 > content > application/json > schema`

390. **File:** `en.yaml`, **Line No:** `35726`, **Line Pos:** `17` - **Line No:** `35726`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > responses > 403 > content > application/json > schema`

391. **File:** `en.yaml`, **Line No:** `35742`, **Line Pos:** `17` - **Line No:** `35742`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/userinfo/issue > post > responses > 500 > content > application/json > schema`

392. **File:** `en.yaml`, **Line No:** `35803`, **Line Pos:** `15` - **Line No:** `35803`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/idtoken/reissue > post > requestBody > content > application/json > schema`

393. **File:** `en.yaml`, **Line No:** `35896`, **Line Pos:** `17` - **Line No:** `35896`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/idtoken/reissue > post > responses > 200 > content > application/json > schema`

394. **File:** `en.yaml`, **Line No:** `35925`, **Line Pos:** `17` - **Line No:** `35925`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/idtoken/reissue > post > responses > 400 > content > application/json > schema`

395. **File:** `en.yaml`, **Line No:** `35941`, **Line Pos:** `17` - **Line No:** `35941`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/idtoken/reissue > post > responses > 401 > content > application/json > schema`

396. **File:** `en.yaml`, **Line No:** `35957`, **Line Pos:** `17` - **Line No:** `35957`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/idtoken/reissue > post > responses > 403 > content > application/json > schema`

397. **File:** `en.yaml`, **Line No:** `35973`, **Line Pos:** `17` - **Line No:** `35973`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/idtoken/reissue > post > responses > 500 > content > application/json > schema`

398. **File:** `en.yaml`, **Line No:** `36005`, **Line Pos:** `15` - **Line No:** `36005`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/gm > post > requestBody > content > application/json > schema`

399. **File:** `en.yaml`, **Line No:** `36079`, **Line Pos:** `17` - **Line No:** `36079`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/gm > post > responses > 200 > content > application/json > schema`

400. **File:** `en.yaml`, **Line No:** `36113`, **Line Pos:** `17` - **Line No:** `36113`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/gm > post > responses > 400 > content > application/json > schema`

401. **File:** `en.yaml`, **Line No:** `36129`, **Line Pos:** `17` - **Line No:** `36129`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/gm > post > responses > 401 > content > application/json > schema`

402. **File:** `en.yaml`, **Line No:** `36145`, **Line Pos:** `17` - **Line No:** `36145`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/gm > post > responses > 403 > content > application/json > schema`

403. **File:** `en.yaml`, **Line No:** `36161`, **Line Pos:** `17` - **Line No:** `36161`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/gm > post > responses > 500 > content > application/json > schema`

404. **File:** `en.yaml`, **Line No:** `36218`, **Line Pos:** `17` - **Line No:** `36218`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/jwks/get > get > responses > 200 > content > application/json > schema`

405. **File:** `en.yaml`, **Line No:** `36256`, **Line Pos:** `17` - **Line No:** `36256`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/jwks/get > get > responses > 400 > content > application/json > schema`

406. **File:** `en.yaml`, **Line No:** `36272`, **Line Pos:** `17` - **Line No:** `36272`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/jwks/get > get > responses > 401 > content > application/json > schema`

407. **File:** `en.yaml`, **Line No:** `36288`, **Line Pos:** `17` - **Line No:** `36288`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/jwks/get > get > responses > 403 > content > application/json > schema`

408. **File:** `en.yaml`, **Line No:** `36304`, **Line Pos:** `17` - **Line No:** `36304`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/jwks/get > get > responses > 500 > content > application/json > schema`

409. **File:** `en.yaml`, **Line No:** `36672`, **Line Pos:** `17` - **Line No:** `36672`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/configuration > get > responses > 400 > content > application/json > schema`

410. **File:** `en.yaml`, **Line No:** `36688`, **Line Pos:** `17` - **Line No:** `36688`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/configuration > get > responses > 401 > content > application/json > schema`

411. **File:** `en.yaml`, **Line No:** `36704`, **Line Pos:** `17` - **Line No:** `36704`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/configuration > get > responses > 403 > content > application/json > schema`

412. **File:** `en.yaml`, **Line No:** `36720`, **Line Pos:** `17` - **Line No:** `36720`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/configuration > get > responses > 500 > content > application/json > schema`

413. **File:** `en.yaml`, **Line No:** `36852`, **Line Pos:** `15` - **Line No:** `36852`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > requestBody > content > application/json > schema`

414. **File:** `en.yaml`, **Line No:** `36853`, **Line Pos:** `19` - **Line No:** `36853`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > requestBody > content > application/json > schema > allOf > 0`

415. **File:** `en.yaml`, **Line No:** `36879`, **Line Pos:** `17` - **Line No:** `36879`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema`

416. **File:** `en.yaml`, **Line No:** `36905`, **Line Pos:** `21` - **Line No:** `36905`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client`

417. **File:** `en.yaml`, **Line No:** `36928`, **Line Pos:** `27` - **Line No:** `36928`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

418. **File:** `en.yaml`, **Line No:** `36945`, **Line Pos:** `27` - **Line No:** `36945`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

419. **File:** `en.yaml`, **Line No:** `37011`, **Line Pos:** `27` - **Line No:** `37011`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > logoUris > items`

420. **File:** `en.yaml`, **Line No:** `37636`, **Line Pos:** `27` - **Line No:** `37636`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > tosUris > items`

421. **File:** `en.yaml`, **Line No:** `37659`, **Line Pos:** `27` - **Line No:** `37659`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > policyUris > items`

422. **File:** `en.yaml`, **Line No:** `37680`, **Line Pos:** `27` - **Line No:** `37680`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > clientUris > items`

423. **File:** `en.yaml`, **Line No:** `37744`, **Line Pos:** `27` - **Line No:** `37744`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > attributes > items`

424. **File:** `en.yaml`, **Line No:** `37755`, **Line Pos:** `25` - **Line No:** `37755`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > extension`

425. **File:** `en.yaml`, **Line No:** `38126`, **Line Pos:** `17` - **Line No:** `38126`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 400 > content > application/json > schema`

426. **File:** `en.yaml`, **Line No:** `38142`, **Line Pos:** `17` - **Line No:** `38142`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 401 > content > application/json > schema`

427. **File:** `en.yaml`, **Line No:** `38158`, **Line Pos:** `17` - **Line No:** `38158`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 403 > content > application/json > schema`

428. **File:** `en.yaml`, **Line No:** `38174`, **Line Pos:** `17` - **Line No:** `38174`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration > post > responses > 500 > content > application/json > schema`

429. **File:** `en.yaml`, **Line No:** `38341`, **Line Pos:** `15` - **Line No:** `38341`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > requestBody > content > application/json > schema`

430. **File:** `en.yaml`, **Line No:** `38342`, **Line Pos:** `19` - **Line No:** `38342`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > requestBody > content > application/json > schema > allOf > 0`

431. **File:** `en.yaml`, **Line No:** `38370`, **Line Pos:** `17` - **Line No:** `38370`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema`

432. **File:** `en.yaml`, **Line No:** `38396`, **Line Pos:** `21` - **Line No:** `38396`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client`

433. **File:** `en.yaml`, **Line No:** `38419`, **Line Pos:** `27` - **Line No:** `38419`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

434. **File:** `en.yaml`, **Line No:** `38436`, **Line Pos:** `27` - **Line No:** `38436`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

435. **File:** `en.yaml`, **Line No:** `38502`, **Line Pos:** `27` - **Line No:** `38502`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > logoUris > items`

436. **File:** `en.yaml`, **Line No:** `39127`, **Line Pos:** `27` - **Line No:** `39127`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > tosUris > items`

437. **File:** `en.yaml`, **Line No:** `39150`, **Line Pos:** `27` - **Line No:** `39150`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > policyUris > items`

438. **File:** `en.yaml`, **Line No:** `39171`, **Line Pos:** `27` - **Line No:** `39171`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > clientUris > items`

439. **File:** `en.yaml`, **Line No:** `39235`, **Line Pos:** `27` - **Line No:** `39235`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > attributes > items`

440. **File:** `en.yaml`, **Line No:** `39246`, **Line Pos:** `25` - **Line No:** `39246`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 200 > content > application/json > schema > properties > client > properties > extension`

441. **File:** `en.yaml`, **Line No:** `39617`, **Line Pos:** `17` - **Line No:** `39617`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 400 > content > application/json > schema`

442. **File:** `en.yaml`, **Line No:** `39633`, **Line Pos:** `17` - **Line No:** `39633`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 401 > content > application/json > schema`

443. **File:** `en.yaml`, **Line No:** `39649`, **Line Pos:** `17` - **Line No:** `39649`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 403 > content > application/json > schema`

444. **File:** `en.yaml`, **Line No:** `39665`, **Line Pos:** `17` - **Line No:** `39665`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/get > post > responses > 500 > content > application/json > schema`

445. **File:** `en.yaml`, **Line No:** `39834`, **Line Pos:** `15` - **Line No:** `39834`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > requestBody > content > application/json > schema`

446. **File:** `en.yaml`, **Line No:** `39835`, **Line Pos:** `19` - **Line No:** `39835`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > requestBody > content > application/json > schema > allOf > 0`

447. **File:** `en.yaml`, **Line No:** `39865`, **Line Pos:** `17` - **Line No:** `39865`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema`

448. **File:** `en.yaml`, **Line No:** `39891`, **Line Pos:** `21` - **Line No:** `39891`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client`

449. **File:** `en.yaml`, **Line No:** `39914`, **Line Pos:** `27` - **Line No:** `39914`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

450. **File:** `en.yaml`, **Line No:** `39931`, **Line Pos:** `27` - **Line No:** `39931`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

451. **File:** `en.yaml`, **Line No:** `39997`, **Line Pos:** `27` - **Line No:** `39997`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > logoUris > items`

452. **File:** `en.yaml`, **Line No:** `40622`, **Line Pos:** `27` - **Line No:** `40622`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > tosUris > items`

453. **File:** `en.yaml`, **Line No:** `40645`, **Line Pos:** `27` - **Line No:** `40645`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > policyUris > items`

454. **File:** `en.yaml`, **Line No:** `40666`, **Line Pos:** `27` - **Line No:** `40666`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > clientUris > items`

455. **File:** `en.yaml`, **Line No:** `40730`, **Line Pos:** `27` - **Line No:** `40730`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > attributes > items`

456. **File:** `en.yaml`, **Line No:** `40741`, **Line Pos:** `25` - **Line No:** `40741`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 200 > content > application/json > schema > properties > client > properties > extension`

457. **File:** `en.yaml`, **Line No:** `41112`, **Line Pos:** `17` - **Line No:** `41112`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 400 > content > application/json > schema`

458. **File:** `en.yaml`, **Line No:** `41128`, **Line Pos:** `17` - **Line No:** `41128`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 401 > content > application/json > schema`

459. **File:** `en.yaml`, **Line No:** `41144`, **Line Pos:** `17` - **Line No:** `41144`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 403 > content > application/json > schema`

460. **File:** `en.yaml`, **Line No:** `41160`, **Line Pos:** `17` - **Line No:** `41160`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/update > post > responses > 500 > content > application/json > schema`

461. **File:** `en.yaml`, **Line No:** `41326`, **Line Pos:** `15` - **Line No:** `41326`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > requestBody > content > application/json > schema`

462. **File:** `en.yaml`, **Line No:** `41327`, **Line Pos:** `19` - **Line No:** `41327`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > requestBody > content > application/json > schema > allOf > 0`

463. **File:** `en.yaml`, **Line No:** `41355`, **Line Pos:** `17` - **Line No:** `41355`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema`

464. **File:** `en.yaml`, **Line No:** `41381`, **Line Pos:** `21` - **Line No:** `41381`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client`

465. **File:** `en.yaml`, **Line No:** `41404`, **Line Pos:** `27` - **Line No:** `41404`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

466. **File:** `en.yaml`, **Line No:** `41421`, **Line Pos:** `27` - **Line No:** `41421`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

467. **File:** `en.yaml`, **Line No:** `41487`, **Line Pos:** `27` - **Line No:** `41487`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > logoUris > items`

468. **File:** `en.yaml`, **Line No:** `42112`, **Line Pos:** `27` - **Line No:** `42112`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > tosUris > items`

469. **File:** `en.yaml`, **Line No:** `42135`, **Line Pos:** `27` - **Line No:** `42135`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > policyUris > items`

470. **File:** `en.yaml`, **Line No:** `42156`, **Line Pos:** `27` - **Line No:** `42156`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > clientUris > items`

471. **File:** `en.yaml`, **Line No:** `42220`, **Line Pos:** `27` - **Line No:** `42220`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > attributes > items`

472. **File:** `en.yaml`, **Line No:** `42231`, **Line Pos:** `25` - **Line No:** `42231`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 200 > content > application/json > schema > properties > client > properties > extension`

473. **File:** `en.yaml`, **Line No:** `42577`, **Line Pos:** `17` - **Line No:** `42577`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 400 > content > application/json > schema`

474. **File:** `en.yaml`, **Line No:** `42593`, **Line Pos:** `17` - **Line No:** `42593`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 401 > content > application/json > schema`

475. **File:** `en.yaml`, **Line No:** `42609`, **Line Pos:** `17` - **Line No:** `42609`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 403 > content > application/json > schema`

476. **File:** `en.yaml`, **Line No:** `42625`, **Line Pos:** `17` - **Line No:** `42625`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/registration/delete > post > responses > 500 > content > application/json > schema`

477. **File:** `en.yaml`, **Line No:** `42994`, **Line Pos:** `15` - **Line No:** `42994`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > requestBody > content > application/json > schema`

478. **File:** `en.yaml`, **Line No:** `43052`, **Line Pos:** `15` - **Line No:** `43052`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > requestBody > content > application/x-www-form-urlencoded > schema`

479. **File:** `en.yaml`, **Line No:** `43110`, **Line Pos:** `17` - **Line No:** `43110`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema`

480. **File:** `en.yaml`, **Line No:** `43155`, **Line Pos:** `23` - **Line No:** `43155`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > scopes > items`

481. **File:** `en.yaml`, **Line No:** `43170`, **Line Pos:** `29` - **Line No:** `43170`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > descriptions > items`

482. **File:** `en.yaml`, **Line No:** `43182`, **Line Pos:** `29` - **Line No:** `43182`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > attributes > items`

483. **File:** `en.yaml`, **Line No:** `43287`, **Line Pos:** `21` - **Line No:** `43287`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

484. **File:** `en.yaml`, **Line No:** `43296`, **Line Pos:** `27` - **Line No:** `43296`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

485. **File:** `en.yaml`, **Line No:** `43367`, **Line Pos:** `23` - **Line No:** `43367`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

486. **File:** `en.yaml`, **Line No:** `43380`, **Line Pos:** `23` - **Line No:** `43380`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

487. **File:** `en.yaml`, **Line No:** `43393`, **Line Pos:** `23` - **Line No:** `43393`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > dynamicScopes > items`

488. **File:** `en.yaml`, **Line No:** `43435`, **Line Pos:** `21` - **Line No:** `43435`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > grant`

489. **File:** `en.yaml`, **Line No:** `43440`, **Line Pos:** `27` - **Line No:** `43440`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > grant > properties > scopes > items`

490. **File:** `en.yaml`, **Line No:** `43459`, **Line Pos:** `25` - **Line No:** `43459`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails`

491. **File:** `en.yaml`, **Line No:** `43468`, **Line Pos:** `31` - **Line No:** `43468`, **Line Pos:** `32`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails > properties > elements > items`

492. **File:** `en.yaml`, **Line No:** `43595`, **Line Pos:** `17` - **Line No:** `43595`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 400 > content > application/json > schema`

493. **File:** `en.yaml`, **Line No:** `43611`, **Line Pos:** `17` - **Line No:** `43611`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 401 > content > application/json > schema`

494. **File:** `en.yaml`, **Line No:** `43627`, **Line Pos:** `17` - **Line No:** `43627`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 403 > content > application/json > schema`

495. **File:** `en.yaml`, **Line No:** `43643`, **Line Pos:** `17` - **Line No:** `43643`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication > post > responses > 500 > content > application/json > schema`

496. **File:** `en.yaml`, **Line No:** `43793`, **Line Pos:** `15` - **Line No:** `43793`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > requestBody > content > application/json > schema`

497. **File:** `en.yaml`, **Line No:** `43805`, **Line Pos:** `15` - **Line No:** `43805`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > requestBody > content > application/x-www-form-urlencoded > schema`

498. **File:** `en.yaml`, **Line No:** `43819`, **Line Pos:** `17` - **Line No:** `43819`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > responses > 200 > content > application/json > schema`

499. **File:** `en.yaml`, **Line No:** `43867`, **Line Pos:** `17` - **Line No:** `43867`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > responses > 400 > content > application/json > schema`

500. **File:** `en.yaml`, **Line No:** `43883`, **Line Pos:** `17` - **Line No:** `43883`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > responses > 401 > content > application/json > schema`

501. **File:** `en.yaml`, **Line No:** `43899`, **Line Pos:** `17` - **Line No:** `43899`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > responses > 403 > content > application/json > schema`

502. **File:** `en.yaml`, **Line No:** `43915`, **Line Pos:** `17` - **Line No:** `43915`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/issue > post > responses > 500 > content > application/json > schema`

503. **File:** `en.yaml`, **Line No:** `44008`, **Line Pos:** `15` - **Line No:** `44008`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > requestBody > content > application/json > schema`

504. **File:** `en.yaml`, **Line No:** `44048`, **Line Pos:** `15` - **Line No:** `44048`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > requestBody > content > application/x-www-form-urlencoded > schema`

505. **File:** `en.yaml`, **Line No:** `44092`, **Line Pos:** `17` - **Line No:** `44092`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > responses > 200 > content > application/json > schema`

506. **File:** `en.yaml`, **Line No:** `44122`, **Line Pos:** `17` - **Line No:** `44122`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > responses > 400 > content > application/json > schema`

507. **File:** `en.yaml`, **Line No:** `44138`, **Line Pos:** `17` - **Line No:** `44138`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > responses > 401 > content > application/json > schema`

508. **File:** `en.yaml`, **Line No:** `44154`, **Line Pos:** `17` - **Line No:** `44154`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > responses > 403 > content > application/json > schema`

509. **File:** `en.yaml`, **Line No:** `44170`, **Line Pos:** `17` - **Line No:** `44170`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/fail > post > responses > 500 > content > application/json > schema`

510. **File:** `en.yaml`, **Line No:** `44337`, **Line Pos:** `15` - **Line No:** `44337`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > requestBody > content > application/json > schema`

511. **File:** `en.yaml`, **Line No:** `44380`, **Line Pos:** `21` - **Line No:** `44380`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > requestBody > content > application/json > schema > properties > properties > items`

512. **File:** `en.yaml`, **Line No:** `44469`, **Line Pos:** `15` - **Line No:** `44469`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > requestBody > content > application/x-www-form-urlencoded > schema`

513. **File:** `en.yaml`, **Line No:** `44512`, **Line Pos:** `21` - **Line No:** `44512`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

514. **File:** `en.yaml`, **Line No:** `44601`, **Line Pos:** `17` - **Line No:** `44601`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 200 > content > application/json > schema`

515. **File:** `en.yaml`, **Line No:** `44704`, **Line Pos:** `21` - **Line No:** `44704`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

516. **File:** `en.yaml`, **Line No:** `44713`, **Line Pos:** `27` - **Line No:** `44713`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

517. **File:** `en.yaml`, **Line No:** `44784`, **Line Pos:** `23` - **Line No:** `44784`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

518. **File:** `en.yaml`, **Line No:** `44797`, **Line Pos:** `23` - **Line No:** `44797`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

519. **File:** `en.yaml`, **Line No:** `44845`, **Line Pos:** `17` - **Line No:** `44845`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 400 > content > application/json > schema`

520. **File:** `en.yaml`, **Line No:** `44861`, **Line Pos:** `17` - **Line No:** `44861`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 401 > content > application/json > schema`

521. **File:** `en.yaml`, **Line No:** `44877`, **Line Pos:** `17` - **Line No:** `44877`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 403 > content > application/json > schema`

522. **File:** `en.yaml`, **Line No:** `44893`, **Line Pos:** `17` - **Line No:** `44893`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/backchannel/authentication/complete > post > responses > 500 > content > application/json > schema`

523. **File:** `en.yaml`, **Line No:** `45050`, **Line Pos:** `15` - **Line No:** `45050`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > requestBody > content > application/json > schema`

524. **File:** `en.yaml`, **Line No:** `45108`, **Line Pos:** `15` - **Line No:** `45108`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > requestBody > content > application/x-www-form-urlencoded > schema`

525. **File:** `en.yaml`, **Line No:** `45166`, **Line Pos:** `17` - **Line No:** `45166`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema`

526. **File:** `en.yaml`, **Line No:** `45214`, **Line Pos:** `23` - **Line No:** `45214`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > scopes > items`

527. **File:** `en.yaml`, **Line No:** `45229`, **Line Pos:** `29` - **Line No:** `45229`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > descriptions > items`

528. **File:** `en.yaml`, **Line No:** `45241`, **Line Pos:** `29` - **Line No:** `45241`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > attributes > items`

529. **File:** `en.yaml`, **Line No:** `45327`, **Line Pos:** `21` - **Line No:** `45327`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

530. **File:** `en.yaml`, **Line No:** `45336`, **Line Pos:** `27` - **Line No:** `45336`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

531. **File:** `en.yaml`, **Line No:** `45407`, **Line Pos:** `23` - **Line No:** `45407`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

532. **File:** `en.yaml`, **Line No:** `45420`, **Line Pos:** `23` - **Line No:** `45420`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

533. **File:** `en.yaml`, **Line No:** `45433`, **Line Pos:** `23` - **Line No:** `45433`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > dynamicScopes > items`

534. **File:** `en.yaml`, **Line No:** `45465`, **Line Pos:** `21` - **Line No:** `45465`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > grant`

535. **File:** `en.yaml`, **Line No:** `45470`, **Line Pos:** `27` - **Line No:** `45470`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > grant > properties > scopes > items`

536. **File:** `en.yaml`, **Line No:** `45489`, **Line Pos:** `25` - **Line No:** `45489`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails`

537. **File:** `en.yaml`, **Line No:** `45498`, **Line Pos:** `31` - **Line No:** `45498`, **Line Pos:** `32`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails > properties > elements > items`

538. **File:** `en.yaml`, **Line No:** `45624`, **Line Pos:** `17` - **Line No:** `45624`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 400 > content > application/json > schema`

539. **File:** `en.yaml`, **Line No:** `45640`, **Line Pos:** `17` - **Line No:** `45640`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 401 > content > application/json > schema`

540. **File:** `en.yaml`, **Line No:** `45656`, **Line Pos:** `17` - **Line No:** `45656`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 403 > content > application/json > schema`

541. **File:** `en.yaml`, **Line No:** `45672`, **Line Pos:** `17` - **Line No:** `45672`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/authorization > post > responses > 500 > content > application/json > schema`

542. **File:** `en.yaml`, **Line No:** `45774`, **Line Pos:** `15` - **Line No:** `45774`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > requestBody > content > application/json > schema`

543. **File:** `en.yaml`, **Line No:** `45786`, **Line Pos:** `15` - **Line No:** `45786`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > requestBody > content > application/x-www-form-urlencoded > schema`

544. **File:** `en.yaml`, **Line No:** `45800`, **Line Pos:** `17` - **Line No:** `45800`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema`

545. **File:** `en.yaml`, **Line No:** `45837`, **Line Pos:** `23` - **Line No:** `45837`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > scopes > items`

546. **File:** `en.yaml`, **Line No:** `45852`, **Line Pos:** `29` - **Line No:** `45852`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > descriptions > items`

547. **File:** `en.yaml`, **Line No:** `45864`, **Line Pos:** `29` - **Line No:** `45864`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > scopes > items > properties > attributes > items`

548. **File:** `en.yaml`, **Line No:** `45906`, **Line Pos:** `21` - **Line No:** `45906`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

549. **File:** `en.yaml`, **Line No:** `45915`, **Line Pos:** `27` - **Line No:** `45915`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

550. **File:** `en.yaml`, **Line No:** `45986`, **Line Pos:** `23` - **Line No:** `45986`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > serviceAttributes > items`

551. **File:** `en.yaml`, **Line No:** `45999`, **Line Pos:** `23` - **Line No:** `45999`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > clientAttributes > items`

552. **File:** `en.yaml`, **Line No:** `46012`, **Line Pos:** `23` - **Line No:** `46012`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > dynamicScopes > items`

553. **File:** `en.yaml`, **Line No:** `46049`, **Line Pos:** `21` - **Line No:** `46049`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > grant`

554. **File:** `en.yaml`, **Line No:** `46054`, **Line Pos:** `27` - **Line No:** `46054`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > grant > properties > scopes > items`

555. **File:** `en.yaml`, **Line No:** `46073`, **Line Pos:** `25` - **Line No:** `46073`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails`

556. **File:** `en.yaml`, **Line No:** `46082`, **Line Pos:** `31` - **Line No:** `46082`, **Line Pos:** `32`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 200 > content > application/json > schema > properties > grant > properties > authorizationDetails > properties > elements > items`

557. **File:** `en.yaml`, **Line No:** `46202`, **Line Pos:** `17` - **Line No:** `46202`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 400 > content > application/json > schema`

558. **File:** `en.yaml`, **Line No:** `46218`, **Line Pos:** `17` - **Line No:** `46218`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 401 > content > application/json > schema`

559. **File:** `en.yaml`, **Line No:** `46234`, **Line Pos:** `17` - **Line No:** `46234`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 403 > content > application/json > schema`

560. **File:** `en.yaml`, **Line No:** `46250`, **Line Pos:** `17` - **Line No:** `46250`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/verification > post > responses > 500 > content > application/json > schema`

561. **File:** `en.yaml`, **Line No:** `46377`, **Line Pos:** `15` - **Line No:** `46377`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > requestBody > content > application/json > schema`

562. **File:** `en.yaml`, **Line No:** `46420`, **Line Pos:** `21` - **Line No:** `46420`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > requestBody > content > application/json > schema > properties > properties > items`

563. **File:** `en.yaml`, **Line No:** `46505`, **Line Pos:** `15` - **Line No:** `46505`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > requestBody > content > application/x-www-form-urlencoded > schema`

564. **File:** `en.yaml`, **Line No:** `46548`, **Line Pos:** `21` - **Line No:** `46548`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

565. **File:** `en.yaml`, **Line No:** `46633`, **Line Pos:** `17` - **Line No:** `46633`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > responses > 200 > content > application/json > schema`

566. **File:** `en.yaml`, **Line No:** `46660`, **Line Pos:** `17` - **Line No:** `46660`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > responses > 400 > content > application/json > schema`

567. **File:** `en.yaml`, **Line No:** `46676`, **Line Pos:** `17` - **Line No:** `46676`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > responses > 401 > content > application/json > schema`

568. **File:** `en.yaml`, **Line No:** `46692`, **Line Pos:** `17` - **Line No:** `46692`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > responses > 403 > content > application/json > schema`

569. **File:** `en.yaml`, **Line No:** `46708`, **Line Pos:** `17` - **Line No:** `46708`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/device/complete > post > responses > 500 > content > application/json > schema`

570. **File:** `en.yaml`, **Line No:** `46800`, **Line Pos:** `17` - **Line No:** `46800`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 200 > content > application/json > schema`

571. **File:** `en.yaml`, **Line No:** `46818`, **Line Pos:** `21` - **Line No:** `46818`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 200 > content > application/json > schema > properties > client`

572. **File:** `en.yaml`, **Line No:** `46834`, **Line Pos:** `27` - **Line No:** `46834`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

573. **File:** `en.yaml`, **Line No:** `46851`, **Line Pos:** `27` - **Line No:** `46851`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

574. **File:** `en.yaml`, **Line No:** `46890`, **Line Pos:** `23` - **Line No:** `46890`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 200 > content > application/json > schema > properties > accessTokens > items`

575. **File:** `en.yaml`, **Line No:** `46948`, **Line Pos:** `29` - **Line No:** `46948`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 200 > content > application/json > schema > properties > accessTokens > items > properties > properties > items`

576. **File:** `en.yaml`, **Line No:** `47023`, **Line Pos:** `17` - **Line No:** `47023`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 400 > content > application/json > schema`

577. **File:** `en.yaml`, **Line No:** `47039`, **Line Pos:** `17` - **Line No:** `47039`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 401 > content > application/json > schema`

578. **File:** `en.yaml`, **Line No:** `47055`, **Line Pos:** `17` - **Line No:** `47055`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 403 > content > application/json > schema`

579. **File:** `en.yaml`, **Line No:** `47071`, **Line Pos:** `17` - **Line No:** `47071`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/get/list > get > responses > 500 > content > application/json > schema`

580. **File:** `en.yaml`, **Line No:** `47131`, **Line Pos:** `15` - **Line No:** `47131`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/json > schema`

581. **File:** `en.yaml`, **Line No:** `47186`, **Line Pos:** `21` - **Line No:** `47186`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/json > schema > properties > properties > items`

582. **File:** `en.yaml`, **Line No:** `47271`, **Line Pos:** `19` - **Line No:** `47271`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/json > schema > properties > authorizationDetails`

583. **File:** `en.yaml`, **Line No:** `47280`, **Line Pos:** `25` - **Line No:** `47280`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

584. **File:** `en.yaml`, **Line No:** `47398`, **Line Pos:** `15` - **Line No:** `47398`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/x-www-form-urlencoded > schema`

585. **File:** `en.yaml`, **Line No:** `47453`, **Line Pos:** `21` - **Line No:** `47453`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

586. **File:** `en.yaml`, **Line No:** `47538`, **Line Pos:** `19` - **Line No:** `47538`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorizationDetails`

587. **File:** `en.yaml`, **Line No:** `47547`, **Line Pos:** `25` - **Line No:** `47547`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorizationDetails > properties > elements > items`

588. **File:** `en.yaml`, **Line No:** `47662`, **Line Pos:** `17` - **Line No:** `47662`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 200 > content > application/json > schema`

589. **File:** `en.yaml`, **Line No:** `47703`, **Line Pos:** `23` - **Line No:** `47703`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 200 > content > application/json > schema > properties > properties > items`

590. **File:** `en.yaml`, **Line No:** `47744`, **Line Pos:** `21` - **Line No:** `47744`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

591. **File:** `en.yaml`, **Line No:** `47753`, **Line Pos:** `27` - **Line No:** `47753`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

592. **File:** `en.yaml`, **Line No:** `47868`, **Line Pos:** `17` - **Line No:** `47868`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 400 > content > application/json > schema`

593. **File:** `en.yaml`, **Line No:** `47884`, **Line Pos:** `17` - **Line No:** `47884`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 401 > content > application/json > schema`

594. **File:** `en.yaml`, **Line No:** `47900`, **Line Pos:** `17` - **Line No:** `47900`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 403 > content > application/json > schema`

595. **File:** `en.yaml`, **Line No:** `47916`, **Line Pos:** `17` - **Line No:** `47916`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/create > post > responses > 500 > content > application/json > schema`

596. **File:** `en.yaml`, **Line No:** `47980`, **Line Pos:** `15` - **Line No:** `47980`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/json > schema`

597. **File:** `en.yaml`, **Line No:** `48009`, **Line Pos:** `21` - **Line No:** `48009`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/json > schema > properties > properties > items`

598. **File:** `en.yaml`, **Line No:** `48065`, **Line Pos:** `19` - **Line No:** `48065`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/json > schema > properties > authorizationDetails`

599. **File:** `en.yaml`, **Line No:** `48074`, **Line Pos:** `25` - **Line No:** `48074`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

600. **File:** `en.yaml`, **Line No:** `48169`, **Line Pos:** `15` - **Line No:** `48169`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/x-www-form-urlencoded > schema`

601. **File:** `en.yaml`, **Line No:** `48198`, **Line Pos:** `21` - **Line No:** `48198`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

602. **File:** `en.yaml`, **Line No:** `48254`, **Line Pos:** `19` - **Line No:** `48254`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorizationDetails`

603. **File:** `en.yaml`, **Line No:** `48263`, **Line Pos:** `25` - **Line No:** `48263`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorizationDetails > properties > elements > items`

604. **File:** `en.yaml`, **Line No:** `48358`, **Line Pos:** `17` - **Line No:** `48358`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 200 > content > application/json > schema`

605. **File:** `en.yaml`, **Line No:** `48386`, **Line Pos:** `23` - **Line No:** `48386`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 200 > content > application/json > schema > properties > properties > items`

606. **File:** `en.yaml`, **Line No:** `48408`, **Line Pos:** `21` - **Line No:** `48408`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 200 > content > application/json > schema > properties > authorizationDetails`

607. **File:** `en.yaml`, **Line No:** `48417`, **Line Pos:** `27` - **Line No:** `48417`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 200 > content > application/json > schema > properties > authorizationDetails > properties > elements > items`

608. **File:** `en.yaml`, **Line No:** `48518`, **Line Pos:** `17` - **Line No:** `48518`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 400 > content > application/json > schema`

609. **File:** `en.yaml`, **Line No:** `48534`, **Line Pos:** `17` - **Line No:** `48534`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 401 > content > application/json > schema`

610. **File:** `en.yaml`, **Line No:** `48550`, **Line Pos:** `17` - **Line No:** `48550`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 403 > content > application/json > schema`

611. **File:** `en.yaml`, **Line No:** `48566`, **Line Pos:** `17` - **Line No:** `48566`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/update > post > responses > 500 > content > application/json > schema`

612. **File:** `en.yaml`, **Line No:** `48638`, **Line Pos:** `17` - **Line No:** `48638`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/delete/{accessTokenIdentifier} > delete > responses > 400 > content > application/json > schema`

613. **File:** `en.yaml`, **Line No:** `48654`, **Line Pos:** `17` - **Line No:** `48654`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/delete/{accessTokenIdentifier} > delete > responses > 401 > content > application/json > schema`

614. **File:** `en.yaml`, **Line No:** `48670`, **Line Pos:** `17` - **Line No:** `48670`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/delete/{accessTokenIdentifier} > delete > responses > 403 > content > application/json > schema`

615. **File:** `en.yaml`, **Line No:** `48686`, **Line Pos:** `17` - **Line No:** `48686`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/delete/{accessTokenIdentifier} > delete > responses > 500 > content > application/json > schema`

616. **File:** `en.yaml`, **Line No:** `48741`, **Line Pos:** `15` - **Line No:** `48741`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > requestBody > content > application/json > schema`

617. **File:** `en.yaml`, **Line No:** `48770`, **Line Pos:** `15` - **Line No:** `48770`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > requestBody > content > application/x-www-form-urlencoded > schema`

618. **File:** `en.yaml`, **Line No:** `48801`, **Line Pos:** `17` - **Line No:** `48801`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > responses > 200 > content > application/json > schema`

619. **File:** `en.yaml`, **Line No:** `48826`, **Line Pos:** `17` - **Line No:** `48826`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > responses > 400 > content > application/json > schema`

620. **File:** `en.yaml`, **Line No:** `48842`, **Line Pos:** `17` - **Line No:** `48842`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > responses > 401 > content > application/json > schema`

621. **File:** `en.yaml`, **Line No:** `48858`, **Line Pos:** `17` - **Line No:** `48858`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > responses > 403 > content > application/json > schema`

622. **File:** `en.yaml`, **Line No:** `48874`, **Line Pos:** `17` - **Line No:** `48874`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/token/revoke > post > responses > 500 > content > application/json > schema`

623. **File:** `en.yaml`, **Line No:** `48934`, **Line Pos:** `15` - **Line No:** `48934`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > requestBody > content > application/json > schema`

624. **File:** `en.yaml`, **Line No:** `48968`, **Line Pos:** `15` - **Line No:** `48968`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > requestBody > content > application/x-www-form-urlencoded > schema`

625. **File:** `en.yaml`, **Line No:** `49001`, **Line Pos:** `17` - **Line No:** `49001`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > responses > 200 > content > application/json > schema`

626. **File:** `en.yaml`, **Line No:** `49045`, **Line Pos:** `17` - **Line No:** `49045`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > responses > 400 > content > application/json > schema`

627. **File:** `en.yaml`, **Line No:** `49061`, **Line Pos:** `17` - **Line No:** `49061`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > responses > 401 > content > application/json > schema`

628. **File:** `en.yaml`, **Line No:** `49077`, **Line Pos:** `17` - **Line No:** `49077`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > responses > 403 > content > application/json > schema`

629. **File:** `en.yaml`, **Line No:** `49093`, **Line Pos:** `17` - **Line No:** `49093`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/jose/verify > post > responses > 500 > content > application/json > schema`

630. **File:** `en.yaml`, **Line No:** `49246`, **Line Pos:** `17` - **Line No:** `49246`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/configuration > post > responses > 200 > content > application/json > schema`

631. **File:** `en.yaml`, **Line No:** `49271`, **Line Pos:** `17` - **Line No:** `49271`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/configuration > post > responses > 400 > content > application/json > schema`

632. **File:** `en.yaml`, **Line No:** `49287`, **Line Pos:** `17` - **Line No:** `49287`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/configuration > post > responses > 401 > content > application/json > schema`

633. **File:** `en.yaml`, **Line No:** `49303`, **Line Pos:** `17` - **Line No:** `49303`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/configuration > post > responses > 403 > content > application/json > schema`

634. **File:** `en.yaml`, **Line No:** `49319`, **Line Pos:** `17` - **Line No:** `49319`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/configuration > post > responses > 500 > content > application/json > schema`

635. **File:** `en.yaml`, **Line No:** `49404`, **Line Pos:** `15` - **Line No:** `49404`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > requestBody > content > application/json > schema`

636. **File:** `en.yaml`, **Line No:** `49416`, **Line Pos:** `15` - **Line No:** `49416`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > requestBody > content > application/x-www-form-urlencoded > schema`

637. **File:** `en.yaml`, **Line No:** `49432`, **Line Pos:** `17` - **Line No:** `49432`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema`

638. **File:** `en.yaml`, **Line No:** `49454`, **Line Pos:** `21` - **Line No:** `49454`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client`

639. **File:** `en.yaml`, **Line No:** `49477`, **Line Pos:** `27` - **Line No:** `49477`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > clientNames > items`

640. **File:** `en.yaml`, **Line No:** `49494`, **Line Pos:** `27` - **Line No:** `49494`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > descriptions > items`

641. **File:** `en.yaml`, **Line No:** `49560`, **Line Pos:** `27` - **Line No:** `49560`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > logoUris > items`

642. **File:** `en.yaml`, **Line No:** `50185`, **Line Pos:** `27` - **Line No:** `50185`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > tosUris > items`

643. **File:** `en.yaml`, **Line No:** `50208`, **Line Pos:** `27` - **Line No:** `50208`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > policyUris > items`

644. **File:** `en.yaml`, **Line No:** `50229`, **Line Pos:** `27` - **Line No:** `50229`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > clientUris > items`

645. **File:** `en.yaml`, **Line No:** `50293`, **Line Pos:** `27` - **Line No:** `50293`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > attributes > items`

646. **File:** `en.yaml`, **Line No:** `50304`, **Line Pos:** `25` - **Line No:** `50304`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 200 > content > application/json > schema > properties > client > properties > extension`

647. **File:** `en.yaml`, **Line No:** `50646`, **Line Pos:** `17` - **Line No:** `50646`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 400 > content > application/json > schema`

648. **File:** `en.yaml`, **Line No:** `50662`, **Line Pos:** `17` - **Line No:** `50662`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 401 > content > application/json > schema`

649. **File:** `en.yaml`, **Line No:** `50678`, **Line Pos:** `17` - **Line No:** `50678`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 403 > content > application/json > schema`

650. **File:** `en.yaml`, **Line No:** `50694`, **Line Pos:** `17` - **Line No:** `50694`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/federation/registration > post > responses > 500 > content > application/json > schema`

651. **File:** `en.yaml`, **Line No:** `50719`, **Line Pos:** `17` - **Line No:** `50719`, **Line Pos:** `18`, **Path:** `# > paths > /api/info > get > responses > 200 > content > application/json > schema`

652. **File:** `en.yaml`, **Line No:** `50749`, **Line Pos:** `17` - **Line No:** `50749`, **Line Pos:** `18`, **Path:** `# > paths > /api/info > get > responses > 400 > content > application/json > schema`

653. **File:** `en.yaml`, **Line No:** `50765`, **Line Pos:** `17` - **Line No:** `50765`, **Line Pos:** `18`, **Path:** `# > paths > /api/info > get > responses > 401 > content > application/json > schema`

654. **File:** `en.yaml`, **Line No:** `50781`, **Line Pos:** `17` - **Line No:** `50781`, **Line Pos:** `18`, **Path:** `# > paths > /api/info > get > responses > 403 > content > application/json > schema`

655. **File:** `en.yaml`, **Line No:** `50797`, **Line Pos:** `17` - **Line No:** `50797`, **Line Pos:** `18`, **Path:** `# > paths > /api/info > get > responses > 500 > content > application/json > schema`

656. **File:** `en.yaml`, **Line No:** `50836`, **Line Pos:** `17` - **Line No:** `50836`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/get/{clientId} > get > responses > 200 > content > application/json > schema`

657. **File:** `en.yaml`, **Line No:** `50847`, **Line Pos:** `17` - **Line No:** `50847`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/get/{clientId} > get > responses > 400 > content > application/json > schema`

658. **File:** `en.yaml`, **Line No:** `50863`, **Line Pos:** `17` - **Line No:** `50863`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/get/{clientId} > get > responses > 401 > content > application/json > schema`

659. **File:** `en.yaml`, **Line No:** `50879`, **Line Pos:** `17` - **Line No:** `50879`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/get/{clientId} > get > responses > 403 > content > application/json > schema`

660. **File:** `en.yaml`, **Line No:** `50895`, **Line Pos:** `17` - **Line No:** `50895`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/get/{clientId} > get > responses > 500 > content > application/json > schema`

661. **File:** `en.yaml`, **Line No:** `50933`, **Line Pos:** `15` - **Line No:** `50933`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/update/{clientId} > put > requestBody > content > application/json > schema`

662. **File:** `en.yaml`, **Line No:** `50956`, **Line Pos:** `17` - **Line No:** `50956`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/update/{clientId} > put > responses > 200 > content > application/json > schema`

663. **File:** `en.yaml`, **Line No:** `50967`, **Line Pos:** `17` - **Line No:** `50967`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/update/{clientId} > put > responses > 400 > content > application/json > schema`

664. **File:** `en.yaml`, **Line No:** `50983`, **Line Pos:** `17` - **Line No:** `50983`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/update/{clientId} > put > responses > 401 > content > application/json > schema`

665. **File:** `en.yaml`, **Line No:** `50999`, **Line Pos:** `17` - **Line No:** `50999`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/update/{clientId} > put > responses > 403 > content > application/json > schema`

666. **File:** `en.yaml`, **Line No:** `51015`, **Line Pos:** `17` - **Line No:** `51015`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/update/{clientId} > put > responses > 500 > content > application/json > schema`

667. **File:** `en.yaml`, **Line No:** `51056`, **Line Pos:** `17` - **Line No:** `51056`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/delete/{clientId} > delete > responses > 400 > content > application/json > schema`

668. **File:** `en.yaml`, **Line No:** `51072`, **Line Pos:** `17` - **Line No:** `51072`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/delete/{clientId} > delete > responses > 401 > content > application/json > schema`

669. **File:** `en.yaml`, **Line No:** `51088`, **Line Pos:** `17` - **Line No:** `51088`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/delete/{clientId} > delete > responses > 403 > content > application/json > schema`

670. **File:** `en.yaml`, **Line No:** `51104`, **Line Pos:** `17` - **Line No:** `51104`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/client/extension/requestable_scopes/delete/{clientId} > delete > responses > 500 > content > application/json > schema`

671. **File:** `en.yaml`, **Line No:** `51136`, **Line Pos:** `15` - **Line No:** `51136`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > requestBody > content > application/json > schema`

672. **File:** `en.yaml`, **Line No:** `51169`, **Line Pos:** `15` - **Line No:** `51169`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > requestBody > content > application/x-www-form-urlencoded > schema`

673. **File:** `en.yaml`, **Line No:** `51206`, **Line Pos:** `17` - **Line No:** `51206`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > responses > 200 > content > application/json > schema`

674. **File:** `en.yaml`, **Line No:** `51223`, **Line Pos:** `21` - **Line No:** `51223`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > responses > 200 > content > application/json > schema > properties > hsk`

675. **File:** `en.yaml`, **Line No:** `51266`, **Line Pos:** `17` - **Line No:** `51266`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > responses > 400 > content > application/json > schema`

676. **File:** `en.yaml`, **Line No:** `51282`, **Line Pos:** `17` - **Line No:** `51282`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > responses > 401 > content > application/json > schema`

677. **File:** `en.yaml`, **Line No:** `51298`, **Line Pos:** `17` - **Line No:** `51298`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > responses > 403 > content > application/json > schema`

678. **File:** `en.yaml`, **Line No:** `51314`, **Line Pos:** `17` - **Line No:** `51314`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/create > post > responses > 500 > content > application/json > schema`

679. **File:** `en.yaml`, **Line No:** `51352`, **Line Pos:** `17` - **Line No:** `51352`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/delete/{handle} > delete > responses > 204 > content > application/json > schema`

680. **File:** `en.yaml`, **Line No:** `51369`, **Line Pos:** `21` - **Line No:** `51369`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/hsk/delete/{handle} > delete > responses > 204 > content > application/json > schema > properties > hsk`

681. **File:** `en.yaml`, **Line No:** `51412`, **Line Pos:** `17` - **Line No:** `51412`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/delete/{handle} > delete > responses > 400 > content > application/json > schema`

682. **File:** `en.yaml`, **Line No:** `51428`, **Line Pos:** `17` - **Line No:** `51428`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/delete/{handle} > delete > responses > 401 > content > application/json > schema`

683. **File:** `en.yaml`, **Line No:** `51444`, **Line Pos:** `17` - **Line No:** `51444`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/delete/{handle} > delete > responses > 403 > content > application/json > schema`

684. **File:** `en.yaml`, **Line No:** `51460`, **Line Pos:** `17` - **Line No:** `51460`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/delete/{handle} > delete > responses > 500 > content > application/json > schema`

685. **File:** `en.yaml`, **Line No:** `51498`, **Line Pos:** `17` - **Line No:** `51498`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/{handle} > get > responses > 200 > content > application/json > schema`

686. **File:** `en.yaml`, **Line No:** `51515`, **Line Pos:** `21` - **Line No:** `51515`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/hsk/get/{handle} > get > responses > 200 > content > application/json > schema > properties > hsk`

687. **File:** `en.yaml`, **Line No:** `51558`, **Line Pos:** `17` - **Line No:** `51558`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/{handle} > get > responses > 400 > content > application/json > schema`

688. **File:** `en.yaml`, **Line No:** `51574`, **Line Pos:** `17` - **Line No:** `51574`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/{handle} > get > responses > 401 > content > application/json > schema`

689. **File:** `en.yaml`, **Line No:** `51590`, **Line Pos:** `17` - **Line No:** `51590`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/{handle} > get > responses > 403 > content > application/json > schema`

690. **File:** `en.yaml`, **Line No:** `51606`, **Line Pos:** `17` - **Line No:** `51606`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/{handle} > get > responses > 500 > content > application/json > schema`

691. **File:** `en.yaml`, **Line No:** `51639`, **Line Pos:** `17` - **Line No:** `51639`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/list > get > responses > 200 > content > application/json > schema`

692. **File:** `en.yaml`, **Line No:** `51657`, **Line Pos:** `23` - **Line No:** `51657`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/hsk/get/list > get > responses > 200 > content > application/json > schema > properties > hsks > items`

693. **File:** `en.yaml`, **Line No:** `51701`, **Line Pos:** `17` - **Line No:** `51701`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/list > get > responses > 400 > content > application/json > schema`

694. **File:** `en.yaml`, **Line No:** `51717`, **Line Pos:** `17` - **Line No:** `51717`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/list > get > responses > 401 > content > application/json > schema`

695. **File:** `en.yaml`, **Line No:** `51733`, **Line Pos:** `17` - **Line No:** `51733`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/list > get > responses > 403 > content > application/json > schema`

696. **File:** `en.yaml`, **Line No:** `51749`, **Line Pos:** `17` - **Line No:** `51749`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/hsk/get/list > get > responses > 500 > content > application/json > schema`

697. **File:** `en.yaml`, **Line No:** `51792`, **Line Pos:** `15` - **Line No:** `51792`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > requestBody > content > application/json > schema`

698. **File:** `en.yaml`, **Line No:** `51803`, **Line Pos:** `15` - **Line No:** `51803`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > requestBody > content > application/x-www-form-urlencoded > schema`

699. **File:** `en.yaml`, **Line No:** `51818`, **Line Pos:** `17` - **Line No:** `51818`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > responses > 200 > content > application/json > schema`

700. **File:** `en.yaml`, **Line No:** `51847`, **Line Pos:** `17` - **Line No:** `51847`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > responses > 400 > content > application/json > schema`

701. **File:** `en.yaml`, **Line No:** `51863`, **Line Pos:** `17` - **Line No:** `51863`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > responses > 401 > content > application/json > schema`

702. **File:** `en.yaml`, **Line No:** `51879`, **Line Pos:** `17` - **Line No:** `51879`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > responses > 403 > content > application/json > schema`

703. **File:** `en.yaml`, **Line No:** `51895`, **Line Pos:** `17` - **Line No:** `51895`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/metadata > post > responses > 500 > content > application/json > schema`

704. **File:** `en.yaml`, **Line No:** `51926`, **Line Pos:** `15` - **Line No:** `51926`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > requestBody > content > application/json > schema`

705. **File:** `en.yaml`, **Line No:** `51937`, **Line Pos:** `15` - **Line No:** `51937`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > requestBody > content > application/x-www-form-urlencoded > schema`

706. **File:** `en.yaml`, **Line No:** `51952`, **Line Pos:** `17` - **Line No:** `51952`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > responses > 200 > content > application/json > schema`

707. **File:** `en.yaml`, **Line No:** `51980`, **Line Pos:** `17` - **Line No:** `51980`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > responses > 400 > content > application/json > schema`

708. **File:** `en.yaml`, **Line No:** `51996`, **Line Pos:** `17` - **Line No:** `51996`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > responses > 401 > content > application/json > schema`

709. **File:** `en.yaml`, **Line No:** `52012`, **Line Pos:** `17` - **Line No:** `52012`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > responses > 403 > content > application/json > schema`

710. **File:** `en.yaml`, **Line No:** `52028`, **Line Pos:** `17` - **Line No:** `52028`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwtissuer > post > responses > 500 > content > application/json > schema`

711. **File:** `en.yaml`, **Line No:** `52059`, **Line Pos:** `15` - **Line No:** `52059`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > requestBody > content > application/json > schema`

712. **File:** `en.yaml`, **Line No:** `52070`, **Line Pos:** `15` - **Line No:** `52070`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > requestBody > content > application/x-www-form-urlencoded > schema`

713. **File:** `en.yaml`, **Line No:** `52085`, **Line Pos:** `17` - **Line No:** `52085`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > responses > 200 > content > application/json > schema`

714. **File:** `en.yaml`, **Line No:** `52113`, **Line Pos:** `17` - **Line No:** `52113`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > responses > 400 > content > application/json > schema`

715. **File:** `en.yaml`, **Line No:** `52129`, **Line Pos:** `17` - **Line No:** `52129`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > responses > 401 > content > application/json > schema`

716. **File:** `en.yaml`, **Line No:** `52145`, **Line Pos:** `17` - **Line No:** `52145`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > responses > 403 > content > application/json > schema`

717. **File:** `en.yaml`, **Line No:** `52161`, **Line Pos:** `17` - **Line No:** `52161`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/jwks > post > responses > 500 > content > application/json > schema`

718. **File:** `en.yaml`, **Line No:** `52192`, **Line Pos:** `15` - **Line No:** `52192`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > requestBody > content > application/json > schema`

719. **File:** `en.yaml`, **Line No:** `52224`, **Line Pos:** `21` - **Line No:** `52224`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > requestBody > content > application/json > schema > properties > properties > items`

720. **File:** `en.yaml`, **Line No:** `52343`, **Line Pos:** `15` - **Line No:** `52343`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > requestBody > content > application/x-www-form-urlencoded > schema`

721. **File:** `en.yaml`, **Line No:** `52375`, **Line Pos:** `21` - **Line No:** `52375`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > properties > items`

722. **File:** `en.yaml`, **Line No:** `52498`, **Line Pos:** `17` - **Line No:** `52498`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 200 > content > application/json > schema`

723. **File:** `en.yaml`, **Line No:** `52515`, **Line Pos:** `21` - **Line No:** `52515`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 200 > content > application/json > schema > properties > info`

724. **File:** `en.yaml`, **Line No:** `52567`, **Line Pos:** `27` - **Line No:** `52567`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 200 > content > application/json > schema > properties > info > properties > properties > items`

725. **File:** `en.yaml`, **Line No:** `52628`, **Line Pos:** `17` - **Line No:** `52628`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 400 > content > application/json > schema`

726. **File:** `en.yaml`, **Line No:** `52644`, **Line Pos:** `17` - **Line No:** `52644`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 401 > content > application/json > schema`

727. **File:** `en.yaml`, **Line No:** `52660`, **Line Pos:** `17` - **Line No:** `52660`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 403 > content > application/json > schema`

728. **File:** `en.yaml`, **Line No:** `52676`, **Line Pos:** `17` - **Line No:** `52676`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/create > post > responses > 500 > content > application/json > schema`

729. **File:** `en.yaml`, **Line No:** `52707`, **Line Pos:** `15` - **Line No:** `52707`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > requestBody > content > application/json > schema`

730. **File:** `en.yaml`, **Line No:** `52714`, **Line Pos:** `15` - **Line No:** `52714`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > requestBody > content > application/x-www-form-urlencoded > schema`

731. **File:** `en.yaml`, **Line No:** `52725`, **Line Pos:** `17` - **Line No:** `52725`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 200 > content > application/json > schema`

732. **File:** `en.yaml`, **Line No:** `52743`, **Line Pos:** `21` - **Line No:** `52743`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 200 > content > application/json > schema > properties > info`

733. **File:** `en.yaml`, **Line No:** `52795`, **Line Pos:** `27` - **Line No:** `52795`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 200 > content > application/json > schema > properties > info > properties > properties > items`

734. **File:** `en.yaml`, **Line No:** `52856`, **Line Pos:** `17` - **Line No:** `52856`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 400 > content > application/json > schema`

735. **File:** `en.yaml`, **Line No:** `52872`, **Line Pos:** `17` - **Line No:** `52872`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 401 > content > application/json > schema`

736. **File:** `en.yaml`, **Line No:** `52888`, **Line Pos:** `17` - **Line No:** `52888`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 403 > content > application/json > schema`

737. **File:** `en.yaml`, **Line No:** `52904`, **Line Pos:** `17` - **Line No:** `52904`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/offer/info > post > responses > 500 > content > application/json > schema`

738. **File:** `en.yaml`, **Line No:** `52935`, **Line Pos:** `15` - **Line No:** `52935`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > requestBody > content > application/json > schema`

739. **File:** `en.yaml`, **Line No:** `52945`, **Line Pos:** `15` - **Line No:** `52945`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > requestBody > content > application/x-www-form-urlencoded > schema`

740. **File:** `en.yaml`, **Line No:** `52959`, **Line Pos:** `17` - **Line No:** `52959`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > responses > 200 > content > application/json > schema`

741. **File:** `en.yaml`, **Line No:** `52980`, **Line Pos:** `21` - **Line No:** `52980`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > responses > 200 > content > application/json > schema > properties > info`

742. **File:** `en.yaml`, **Line No:** `53004`, **Line Pos:** `17` - **Line No:** `53004`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > responses > 400 > content > application/json > schema`

743. **File:** `en.yaml`, **Line No:** `53020`, **Line Pos:** `17` - **Line No:** `53020`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > responses > 401 > content > application/json > schema`

744. **File:** `en.yaml`, **Line No:** `53036`, **Line Pos:** `17` - **Line No:** `53036`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > responses > 403 > content > application/json > schema`

745. **File:** `en.yaml`, **Line No:** `53052`, **Line Pos:** `17` - **Line No:** `53052`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/parse > post > responses > 500 > content > application/json > schema`

746. **File:** `en.yaml`, **Line No:** `53083`, **Line Pos:** `15` - **Line No:** `53083`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > requestBody > content > application/json > schema`

747. **File:** `en.yaml`, **Line No:** `53089`, **Line Pos:** `19` - **Line No:** `53089`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > requestBody > content > application/json > schema > properties > order`

748. **File:** `en.yaml`, **Line No:** `53115`, **Line Pos:** `17` - **Line No:** `53115`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > responses > 200 > content > application/json > schema`

749. **File:** `en.yaml`, **Line No:** `53149`, **Line Pos:** `17` - **Line No:** `53149`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > responses > 400 > content > application/json > schema`

750. **File:** `en.yaml`, **Line No:** `53165`, **Line Pos:** `17` - **Line No:** `53165`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > responses > 401 > content > application/json > schema`

751. **File:** `en.yaml`, **Line No:** `53181`, **Line Pos:** `17` - **Line No:** `53181`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > responses > 403 > content > application/json > schema`

752. **File:** `en.yaml`, **Line No:** `53197`, **Line Pos:** `17` - **Line No:** `53197`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/single/issue > post > responses > 500 > content > application/json > schema`

753. **File:** `en.yaml`, **Line No:** `53228`, **Line Pos:** `15` - **Line No:** `53228`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > requestBody > content > application/json > schema`

754. **File:** `en.yaml`, **Line No:** `53238`, **Line Pos:** `15` - **Line No:** `53238`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > requestBody > content > application/x-www-form-urlencoded > schema`

755. **File:** `en.yaml`, **Line No:** `53252`, **Line Pos:** `17` - **Line No:** `53252`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > responses > 200 > content > application/json > schema`

756. **File:** `en.yaml`, **Line No:** `53275`, **Line Pos:** `23` - **Line No:** `53275`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > responses > 200 > content > application/json > schema > properties > info > items`

757. **File:** `en.yaml`, **Line No:** `53302`, **Line Pos:** `17` - **Line No:** `53302`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > responses > 400 > content > application/json > schema`

758. **File:** `en.yaml`, **Line No:** `53318`, **Line Pos:** `17` - **Line No:** `53318`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > responses > 401 > content > application/json > schema`

759. **File:** `en.yaml`, **Line No:** `53334`, **Line Pos:** `17` - **Line No:** `53334`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > responses > 403 > content > application/json > schema`

760. **File:** `en.yaml`, **Line No:** `53350`, **Line Pos:** `17` - **Line No:** `53350`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/parse > post > responses > 500 > content > application/json > schema`

761. **File:** `en.yaml`, **Line No:** `53381`, **Line Pos:** `15` - **Line No:** `53381`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > requestBody > content > application/json > schema`

762. **File:** `en.yaml`, **Line No:** `53389`, **Line Pos:** `21` - **Line No:** `53389`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > requestBody > content > application/json > schema > properties > orders > items`

763. **File:** `en.yaml`, **Line No:** `53416`, **Line Pos:** `17` - **Line No:** `53416`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > responses > 200 > content > application/json > schema`

764. **File:** `en.yaml`, **Line No:** `53445`, **Line Pos:** `17` - **Line No:** `53445`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > responses > 400 > content > application/json > schema`

765. **File:** `en.yaml`, **Line No:** `53461`, **Line Pos:** `17` - **Line No:** `53461`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > responses > 401 > content > application/json > schema`

766. **File:** `en.yaml`, **Line No:** `53477`, **Line Pos:** `17` - **Line No:** `53477`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > responses > 403 > content > application/json > schema`

767. **File:** `en.yaml`, **Line No:** `53493`, **Line Pos:** `17` - **Line No:** `53493`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/batch/issue > post > responses > 500 > content > application/json > schema`

768. **File:** `en.yaml`, **Line No:** `53524`, **Line Pos:** `15` - **Line No:** `53524`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > requestBody > content > application/json > schema`

769. **File:** `en.yaml`, **Line No:** `53534`, **Line Pos:** `15` - **Line No:** `53534`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > requestBody > content > application/x-www-form-urlencoded > schema`

770. **File:** `en.yaml`, **Line No:** `53548`, **Line Pos:** `17` - **Line No:** `53548`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > responses > 200 > content > application/json > schema`

771. **File:** `en.yaml`, **Line No:** `53569`, **Line Pos:** `21` - **Line No:** `53569`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > responses > 200 > content > application/json > schema > properties > info`

772. **File:** `en.yaml`, **Line No:** `53594`, **Line Pos:** `17` - **Line No:** `53594`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > responses > 400 > content > application/json > schema`

773. **File:** `en.yaml`, **Line No:** `53610`, **Line Pos:** `17` - **Line No:** `53610`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > responses > 401 > content > application/json > schema`

774. **File:** `en.yaml`, **Line No:** `53626`, **Line Pos:** `17` - **Line No:** `53626`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > responses > 403 > content > application/json > schema`

775. **File:** `en.yaml`, **Line No:** `53642`, **Line Pos:** `17` - **Line No:** `53642`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/parse > post > responses > 500 > content > application/json > schema`

776. **File:** `en.yaml`, **Line No:** `53673`, **Line Pos:** `15` - **Line No:** `53673`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > requestBody > content > application/json > schema`

777. **File:** `en.yaml`, **Line No:** `53676`, **Line Pos:** `19` - **Line No:** `53676`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > requestBody > content > application/json > schema > properties > order`

778. **File:** `en.yaml`, **Line No:** `53702`, **Line Pos:** `17` - **Line No:** `53702`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > responses > 200 > content > application/json > schema`

779. **File:** `en.yaml`, **Line No:** `53730`, **Line Pos:** `17` - **Line No:** `53730`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > responses > 400 > content > application/json > schema`

780. **File:** `en.yaml`, **Line No:** `53746`, **Line Pos:** `17` - **Line No:** `53746`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > responses > 401 > content > application/json > schema`

781. **File:** `en.yaml`, **Line No:** `53762`, **Line Pos:** `17` - **Line No:** `53762`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > responses > 403 > content > application/json > schema`

782. **File:** `en.yaml`, **Line No:** `53778`, **Line Pos:** `17` - **Line No:** `53778`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/vci/deferred/issue > post > responses > 500 > content > application/json > schema`

783. **File:** `en.yaml`, **Line No:** `53807`, **Line Pos:** `15` - **Line No:** `53807`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > requestBody > content > application/json > schema`

784. **File:** `en.yaml`, **Line No:** `53816`, **Line Pos:** `15` - **Line No:** `53816`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > requestBody > content > application/x-www-form-urlencoded > schema`

785. **File:** `en.yaml`, **Line No:** `53829`, **Line Pos:** `17` - **Line No:** `53829`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > responses > 200 > content > application/json > schema`

786. **File:** `en.yaml`, **Line No:** `53853`, **Line Pos:** `17` - **Line No:** `53853`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > responses > 400 > content > application/json > schema`

787. **File:** `en.yaml`, **Line No:** `53869`, **Line Pos:** `17` - **Line No:** `53869`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > responses > 401 > content > application/json > schema`

788. **File:** `en.yaml`, **Line No:** `53885`, **Line Pos:** `17` - **Line No:** `53885`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > responses > 403 > content > application/json > schema`

789. **File:** `en.yaml`, **Line No:** `53901`, **Line Pos:** `17` - **Line No:** `53901`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/info > get > responses > 500 > content > application/json > schema`

790. **File:** `en.yaml`, **Line No:** `53930`, **Line Pos:** `15` - **Line No:** `53930`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > requestBody > content > application/json > schema`

791. **File:** `en.yaml`, **Line No:** `53943`, **Line Pos:** `15` - **Line No:** `53943`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > requestBody > content > application/x-www-form-urlencoded > schema`

792. **File:** `en.yaml`, **Line No:** `53960`, **Line Pos:** `17` - **Line No:** `53960`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > responses > 200 > content > application/json > schema`

793. **File:** `en.yaml`, **Line No:** `53984`, **Line Pos:** `17` - **Line No:** `53984`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > responses > 400 > content > application/json > schema`

794. **File:** `en.yaml`, **Line No:** `54000`, **Line Pos:** `17` - **Line No:** `54000`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > responses > 401 > content > application/json > schema`

795. **File:** `en.yaml`, **Line No:** `54016`, **Line Pos:** `17` - **Line No:** `54016`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > responses > 403 > content > application/json > schema`

796. **File:** `en.yaml`, **Line No:** `54032`, **Line Pos:** `17` - **Line No:** `54032`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/auth/authorization/ticket/update > post > responses > 500 > content > application/json > schema`

797. **File:** `en.yaml`, **Line No:** `54112`, **Line Pos:** `15` - **Line No:** `54112`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/nativesso > post > requestBody > content > application/json > schema`

798. **File:** `en.yaml`, **Line No:** `54188`, **Line Pos:** `17` - **Line No:** `54188`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso > post > responses > 200 > content > application/json > schema`

799. **File:** `en.yaml`, **Line No:** `54224`, **Line Pos:** `17` - **Line No:** `54224`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso > post > responses > 400 > content > application/json > schema`

800. **File:** `en.yaml`, **Line No:** `54240`, **Line Pos:** `17` - **Line No:** `54240`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso > post > responses > 401 > content > application/json > schema`

801. **File:** `en.yaml`, **Line No:** `54256`, **Line Pos:** `17` - **Line No:** `54256`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso > post > responses > 403 > content > application/json > schema`

802. **File:** `en.yaml`, **Line No:** `54272`, **Line Pos:** `17` - **Line No:** `54272`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso > post > responses > 500 > content > application/json > schema`

803. **File:** `en.yaml`, **Line No:** `54344`, **Line Pos:** `15` - **Line No:** `54344`, **Line Pos:** `16`, **Path:** `# > paths > /api/{serviceId}/nativesso/logout > post > requestBody > content > application/json > schema`

804. **File:** `en.yaml`, **Line No:** `54360`, **Line Pos:** `17` - **Line No:** `54360`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso/logout > post > responses > 200 > content > application/json > schema`

805. **File:** `en.yaml`, **Line No:** `54390`, **Line Pos:** `17` - **Line No:** `54390`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso/logout > post > responses > 400 > content > application/json > schema`

806. **File:** `en.yaml`, **Line No:** `54406`, **Line Pos:** `17` - **Line No:** `54406`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso/logout > post > responses > 401 > content > application/json > schema`

807. **File:** `en.yaml`, **Line No:** `54422`, **Line Pos:** `17` - **Line No:** `54422`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso/logout > post > responses > 403 > content > application/json > schema`

808. **File:** `en.yaml`, **Line No:** `54438`, **Line Pos:** `17` - **Line No:** `54438`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/nativesso/logout > post > responses > 500 > content > application/json > schema`

809. **File:** `en.yaml`, **Line No:** `54548`, **Line Pos:** `13` - **Line No:** `54548`, **Line Pos:** `14`, **Path:** `# > components > schemas > AccessToken > properties > properties > items`

810. **File:** `en.yaml`, **Line No:** `54587`, **Line Pos:** `13` - **Line No:** `54587`, **Line Pos:** `14`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items`

811. **File:** `en.yaml`, **Line No:** `54833`, **Line Pos:** `13` - **Line No:** `54833`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > clientNames > items`

812. **File:** `en.yaml`, **Line No:** `54850`, **Line Pos:** `13` - **Line No:** `54850`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > descriptions > items`

813. **File:** `en.yaml`, **Line No:** `54916`, **Line Pos:** `13` - **Line No:** `54916`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > logoUris > items`

814. **File:** `en.yaml`, **Line No:** `55541`, **Line Pos:** `13` - **Line No:** `55541`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > tosUris > items`

815. **File:** `en.yaml`, **Line No:** `55564`, **Line Pos:** `13` - **Line No:** `55564`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > policyUris > items`

816. **File:** `en.yaml`, **Line No:** `55585`, **Line Pos:** `13` - **Line No:** `55585`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > clientUris > items`

817. **File:** `en.yaml`, **Line No:** `55649`, **Line Pos:** `13` - **Line No:** `55649`, **Line Pos:** `14`, **Path:** `# > components > schemas > Client > properties > attributes > items`

818. **File:** `en.yaml`, **Line No:** `55660`, **Line Pos:** `11` - **Line No:** `55660`, **Line Pos:** `12`, **Path:** `# > components > schemas > Client > properties > extension`

819. **File:** `en.yaml`, **Line No:** `56183`, **Line Pos:** `13` - **Line No:** `56183`, **Line Pos:** `14`, **Path:** `# > components > schemas > Scope > properties > descriptions > items`

820. **File:** `en.yaml`, **Line No:** `56195`, **Line Pos:** `13` - **Line No:** `56195`, **Line Pos:** `14`, **Path:** `# > components > schemas > Scope > properties > attributes > items`

821. **File:** `en.yaml`, **Line No:** `56242`, **Line Pos:** `13` - **Line No:** `56242`, **Line Pos:** `14`, **Path:** `# > components > schemas > Service > properties > metadata > items`

822. **File:** `en.yaml`, **Line No:** `56621`, **Line Pos:** `13` - **Line No:** `56621`, **Line Pos:** `14`, **Path:** `# > components > schemas > Service > properties > mtlsEndpointAliases > items`

823. **File:** `en.yaml`, **Line No:** `56741`, **Line Pos:** `13` - **Line No:** `56741`, **Line Pos:** `14`, **Path:** `# > components > schemas > Service > properties > supportedScopes > items`

824. **File:** `en.yaml`, **Line No:** `56756`, **Line Pos:** `19` - **Line No:** `56756`, **Line Pos:** `20`, **Path:** `# > components > schemas > Service > properties > supportedScopes > items > properties > descriptions > items`

825. **File:** `en.yaml`, **Line No:** `56768`, **Line Pos:** `19` - **Line No:** `56768`, **Line Pos:** `20`, **Path:** `# > components > schemas > Service > properties > supportedScopes > items > properties > attributes > items`

826. **File:** `en.yaml`, **Line No:** `57182`, **Line Pos:** `13` - **Line No:** `57182`, **Line Pos:** `14`, **Path:** `# > components > schemas > Service > properties > attributes > items`

827. **File:** `en.yaml`, **Line No:** `57358`, **Line Pos:** `13` - **Line No:** `57358`, **Line Pos:** `14`, **Path:** `# > components > schemas > Service > properties > hsks > items`

828. **File:** `en.yaml`, **Line No:** `57723`, **Line Pos:** `13` - **Line No:** `57723`, **Line Pos:** `14`, **Path:** `# > components > schemas > Service > properties > trustAnchors > items`

829. **File:** `en.yaml`, **Line No:** `57866`, **Line Pos:** `11` - **Line No:** `57866`, **Line Pos:** `12`, **Path:** `# > components > schemas > Service > properties > credentialIssuerMetadata`

830. **File:** `en.yaml`, **Line No:** `58067`, **Line Pos:** `13` - **Line No:** `58067`, **Line Pos:** `14`, **Path:** `# > components > schemas > CredentialOfferInfo > properties > properties > items`

831. **File:** `en_test.yaml`, **Line No:** `34`, **Line Pos:** `17` - **Line No:** `34`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema`

832. **File:** `en_test.yaml`, **Line No:** `67`, **Line Pos:** `23` - **Line No:** `67`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata > items`

833. **File:** `en_test.yaml`, **Line No:** `446`, **Line Pos:** `23` - **Line No:** `446`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

834. **File:** `en_test.yaml`, **Line No:** `566`, **Line Pos:** `23` - **Line No:** `566`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

835. **File:** `en_test.yaml`, **Line No:** `581`, **Line Pos:** `29` - **Line No:** `581`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

836. **File:** `en_test.yaml`, **Line No:** `593`, **Line Pos:** `29` - **Line No:** `593`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

837. **File:** `en_test.yaml`, **Line No:** `1007`, **Line Pos:** `23` - **Line No:** `1007`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes > items`

838. **File:** `en_test.yaml`, **Line No:** `1183`, **Line Pos:** `23` - **Line No:** `1183`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items`

839. **File:** `en_test.yaml`, **Line No:** `1548`, **Line Pos:** `23` - **Line No:** `1548`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

840. **File:** `en_test.yaml`, **Line No:** `1691`, **Line Pos:** `21` - **Line No:** `1691`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

841. **File:** `en_test.yaml`, **Line No:** `1863`, **Line Pos:** `17` - **Line No:** `1863`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 400 > content > application/json > schema`

842. **File:** `en_test.yaml`, **Line No:** `1879`, **Line Pos:** `17` - **Line No:** `1879`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 401 > content > application/json > schema`

843. **File:** `en_test.yaml`, **Line No:** `1895`, **Line Pos:** `17` - **Line No:** `1895`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 403 > content > application/json > schema`

844. **File:** `en_test.yaml`, **Line No:** `1911`, **Line Pos:** `17` - **Line No:** `1911`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 500 > content > application/json > schema`

845. **File:** `en_test.yaml`, **Line No:** `1981`, **Line Pos:** `17` - **Line No:** `1981`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema`

846. **File:** `en_test.yaml`, **Line No:** `2004`, **Line Pos:** `23` - **Line No:** `2004`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items`

847. **File:** `en_test.yaml`, **Line No:** `2037`, **Line Pos:** `29` - **Line No:** `2037`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata > items`

848. **File:** `en_test.yaml`, **Line No:** `2416`, **Line Pos:** `29` - **Line No:** `2416`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items`

849. **File:** `en_test.yaml`, **Line No:** `2536`, **Line Pos:** `29` - **Line No:** `2536`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items`

850. **File:** `en_test.yaml`, **Line No:** `2551`, **Line Pos:** `35` - **Line No:** `2551`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions > items`

851. **File:** `en_test.yaml`, **Line No:** `2563`, **Line Pos:** `35` - **Line No:** `2563`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes > items`

852. **File:** `en_test.yaml`, **Line No:** `2977`, **Line Pos:** `29` - **Line No:** `2977`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes > items`

853. **File:** `en_test.yaml`, **Line No:** `3153`, **Line Pos:** `29` - **Line No:** `3153`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items`

854. **File:** `en_test.yaml`, **Line No:** `3518`, **Line Pos:** `29` - **Line No:** `3518`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors > items`

855. **File:** `en_test.yaml`, **Line No:** `3661`, **Line Pos:** `27` - **Line No:** `3661`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata`

856. **File:** `en_test.yaml`, **Line No:** `3843`, **Line Pos:** `17` - **Line No:** `3843`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 400 > content > application/json > schema`

857. **File:** `en_test.yaml`, **Line No:** `3859`, **Line Pos:** `17` - **Line No:** `3859`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 401 > content > application/json > schema`

858. **File:** `en_test.yaml`, **Line No:** `3875`, **Line Pos:** `17` - **Line No:** `3875`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 403 > content > application/json > schema`

859. **File:** `en_test.yaml`, **Line No:** `3891`, **Line Pos:** `17` - **Line No:** `3891`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 500 > content > application/json > schema`

860. **File:** `en_test.yaml`, **Line No:** `3940`, **Line Pos:** `15` - **Line No:** `3940`, **Line Pos:** `16`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema`

861. **File:** `en_test.yaml`, **Line No:** `3973`, **Line Pos:** `21` - **Line No:** `3973`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata > items`

862. **File:** `en_test.yaml`, **Line No:** `4352`, **Line Pos:** `21` - **Line No:** `4352`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items`

863. **File:** `en_test.yaml`, **Line No:** `4472`, **Line Pos:** `21` - **Line No:** `4472`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items`

864. **File:** `en_test.yaml`, **Line No:** `4487`, **Line Pos:** `27` - **Line No:** `4487`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

865. **File:** `en_test.yaml`, **Line No:** `4499`, **Line Pos:** `27` - **Line No:** `4499`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

866. **File:** `en_test.yaml`, **Line No:** `4913`, **Line Pos:** `21` - **Line No:** `4913`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > attributes > items`

867. **File:** `en_test.yaml`, **Line No:** `5089`, **Line Pos:** `21` - **Line No:** `5089`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > hsks > items`

868. **File:** `en_test.yaml`, **Line No:** `5454`, **Line Pos:** `21` - **Line No:** `5454`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > trustAnchors > items`

869. **File:** `en_test.yaml`, **Line No:** `5597`, **Line Pos:** `19` - **Line No:** `5597`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata`

870. **File:** `en_test.yaml`, **Line No:** `5700`, **Line Pos:** `15` - **Line No:** `5700`, **Line Pos:** `16`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema`

871. **File:** `en_test.yaml`, **Line No:** `5733`, **Line Pos:** `21` - **Line No:** `5733`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > metadata > items`

872. **File:** `en_test.yaml`, **Line No:** `6112`, **Line Pos:** `21` - **Line No:** `6112`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > mtlsEndpointAliases > items`

873. **File:** `en_test.yaml`, **Line No:** `6232`, **Line Pos:** `21` - **Line No:** `6232`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items`

874. **File:** `en_test.yaml`, **Line No:** `6247`, **Line Pos:** `27` - **Line No:** `6247`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > descriptions > items`

875. **File:** `en_test.yaml`, **Line No:** `6259`, **Line Pos:** `27` - **Line No:** `6259`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > attributes > items`

876. **File:** `en_test.yaml`, **Line No:** `6673`, **Line Pos:** `21` - **Line No:** `6673`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > attributes > items`

877. **File:** `en_test.yaml`, **Line No:** `6849`, **Line Pos:** `21` - **Line No:** `6849`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > hsks > items`

878. **File:** `en_test.yaml`, **Line No:** `7214`, **Line Pos:** `21` - **Line No:** `7214`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > trustAnchors > items`

879. **File:** `en_test.yaml`, **Line No:** `7357`, **Line Pos:** `19` - **Line No:** `7357`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata`

880. **File:** `en_test.yaml`, **Line No:** `7429`, **Line Pos:** `17` - **Line No:** `7429`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema`

881. **File:** `en_test.yaml`, **Line No:** `7462`, **Line Pos:** `23` - **Line No:** `7462`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > metadata > items`

882. **File:** `en_test.yaml`, **Line No:** `7841`, **Line Pos:** `23` - **Line No:** `7841`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

883. **File:** `en_test.yaml`, **Line No:** `7961`, **Line Pos:** `23` - **Line No:** `7961`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

884. **File:** `en_test.yaml`, **Line No:** `7976`, **Line Pos:** `29` - **Line No:** `7976`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

885. **File:** `en_test.yaml`, **Line No:** `7988`, **Line Pos:** `29` - **Line No:** `7988`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

886. **File:** `en_test.yaml`, **Line No:** `8402`, **Line Pos:** `23` - **Line No:** `8402`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > attributes > items`

887. **File:** `en_test.yaml`, **Line No:** `8578`, **Line Pos:** `23` - **Line No:** `8578`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > hsks > items`

888. **File:** `en_test.yaml`, **Line No:** `8943`, **Line Pos:** `23` - **Line No:** `8943`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

889. **File:** `en_test.yaml`, **Line No:** `9086`, **Line Pos:** `21` - **Line No:** `9086`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

890. **File:** `en_test.yaml`, **Line No:** `9249`, **Line Pos:** `17` - **Line No:** `9249`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 400 > content > application/json > schema`

891. **File:** `en_test.yaml`, **Line No:** `9265`, **Line Pos:** `17` - **Line No:** `9265`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 401 > content > application/json > schema`

892. **File:** `en_test.yaml`, **Line No:** `9281`, **Line Pos:** `17` - **Line No:** `9281`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 403 > content > application/json > schema`

893. **File:** `en_test.yaml`, **Line No:** `9297`, **Line Pos:** `17` - **Line No:** `9297`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 500 > content > application/json > schema`

894. **File:** `en_test.yaml`, **Line No:** `9401`, **Line Pos:** `13` - **Line No:** `9401`, **Line Pos:** `14`, **Path:** `# > components > schemas > AccessToken > properties > properties > items`

895. **File:** `en_test.yaml`, **Line No:** `9440`, **Line Pos:** `13` - **Line No:** `9440`, **Line Pos:** `14`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items`


### <a id="warn-issue-no-6---inline-enum-schema-definition-found-234"></a> `Warn` Issue No. 6 - Inline enum schema definition found. (234)

| Property | Value |
| -------- | ----- |
| Rule Id | `no-inline-enum-schema-definition` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Schemas |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

Either define a title property alongside the `enum` property or the schema definitions must be added globally in the components/schemas section with a unique name and then referenced throughout the API document with that name. Inline definitions of enum schemas are not recommended as for auto-generating SDKs/documentation the names of such schemas are deduced from the parent objects in which they are declared inline. The names deduced this way may not be user-friendly and can conflict with other definitions resulting in name duplication. This behavior can affect your output quality.

#### <a id="tips-6"></a> Tips

* Add `title` property alongside the `enum` property in the schema definition.
* Remove the inline enum schema definition and relocate it to the components/schemas section.
* Define the enum schema globally in the components/schemas section with a unique name. Then reference it using $ref in your current object with a path like '#/components/schemas/<global name>'.
* Ensure that no other inline enum schemas are defined.
* If you wish to retain the inline schema definition, try adding a `title` property in the Schema Object definition with a unique name to improve output.

#### <a id="for-more-information-6"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schema-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#componentsObject
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-234"></a> Affected Components (`234`)

1. **File:** `en.yaml`, **Line No:** `246`, **Line Pos:** `23` - **Line No:** `246`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedGrantTypes > items`

2. **File:** `en.yaml`, **Line No:** `267`, **Line Pos:** `23` - **Line No:** `267`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

3. **File:** `en.yaml`, **Line No:** `295`, **Line Pos:** `23` - **Line No:** `295`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

4. **File:** `en.yaml`, **Line No:** `348`, **Line Pos:** `23` - **Line No:** `348`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDisplays > items`

5. **File:** `en.yaml`, **Line No:** `413`, **Line Pos:** `23` - **Line No:** `413`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods > items`

6. **File:** `en.yaml`, **Line No:** `450`, **Line Pos:** `23` - **Line No:** `450`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

7. **File:** `en.yaml`, **Line No:** `477`, **Line Pos:** `23` - **Line No:** `477`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

8. **File:** `en.yaml`, **Line No:** `615`, **Line Pos:** `21` - **Line No:** `615`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenSignAlg`

9. **File:** `en.yaml`, **Line No:** `765`, **Line Pos:** `23` - **Line No:** `765`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

10. **File:** `en.yaml`, **Line No:** `977`, **Line Pos:** `23` - **Line No:** `977`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

11. **File:** `en.yaml`, **Line No:** `1068`, **Line Pos:** `21` - **Line No:** `1068`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userCodeCharset`

12. **File:** `en.yaml`, **Line No:** `1114`, **Line Pos:** `21` - **Line No:** `1114`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

13. **File:** `en.yaml`, **Line No:** `1534`, **Line Pos:** `23` - **Line No:** `1534`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAttachments > items`

14. **File:** `en.yaml`, **Line No:** `1606`, **Line Pos:** `23` - **Line No:** `1606`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

15. **File:** `en.yaml`, **Line No:** `1756`, **Line Pos:** `23` - **Line No:** `1756`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedPromptValues > items`

16. **File:** `en.yaml`, **Line No:** `1783`, **Line Pos:** `23` - **Line No:** `1783`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > fapiModes > items`

17. **File:** `en.yaml`, **Line No:** `2216`, **Line Pos:** `29` - **Line No:** `2216`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedGrantTypes > items`

18. **File:** `en.yaml`, **Line No:** `2237`, **Line Pos:** `29` - **Line No:** `2237`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedResponseTypes > items`

19. **File:** `en.yaml`, **Line No:** `2265`, **Line Pos:** `29` - **Line No:** `2265`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedServiceProfiles > items`

20. **File:** `en.yaml`, **Line No:** `2318`, **Line Pos:** `29` - **Line No:** `2318`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDisplays > items`

21. **File:** `en.yaml`, **Line No:** `2383`, **Line Pos:** `29` - **Line No:** `2383`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTokenAuthMethods > items`

22. **File:** `en.yaml`, **Line No:** `2420`, **Line Pos:** `29` - **Line No:** `2420`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedRevocationAuthMethods > items`

23. **File:** `en.yaml`, **Line No:** `2447`, **Line Pos:** `29` - **Line No:** `2447`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIntrospectionAuthMethods > items`

24. **File:** `en.yaml`, **Line No:** `2585`, **Line Pos:** `27` - **Line No:** `2585`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenSignAlg`

25. **File:** `en.yaml`, **Line No:** `2735`, **Line Pos:** `29` - **Line No:** `2735`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimTypes > items`

26. **File:** `en.yaml`, **Line No:** `2947`, **Line Pos:** `29` - **Line No:** `2947`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedBackchannelTokenDeliveryModes > items`

27. **File:** `en.yaml`, **Line No:** `3038`, **Line Pos:** `27` - **Line No:** `3038`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userCodeCharset`

28. **File:** `en.yaml`, **Line No:** `3084`, **Line Pos:** `27` - **Line No:** `3084`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > verifiedClaimsValidationSchemaSet`

29. **File:** `en.yaml`, **Line No:** `3504`, **Line Pos:** `29` - **Line No:** `3504`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAttachments > items`

30. **File:** `en.yaml`, **Line No:** `3576`, **Line Pos:** `29` - **Line No:** `3576`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClientRegistrationTypes > items`

31. **File:** `en.yaml`, **Line No:** `3726`, **Line Pos:** `29` - **Line No:** `3726`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedPromptValues > items`

32. **File:** `en.yaml`, **Line No:** `3753`, **Line Pos:** `29` - **Line No:** `3753`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > fapiModes > items`

33. **File:** `en.yaml`, **Line No:** `4152`, **Line Pos:** `21` - **Line No:** `4152`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedGrantTypes > items`

34. **File:** `en.yaml`, **Line No:** `4173`, **Line Pos:** `21` - **Line No:** `4173`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedResponseTypes > items`

35. **File:** `en.yaml`, **Line No:** `4201`, **Line Pos:** `21` - **Line No:** `4201`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedServiceProfiles > items`

36. **File:** `en.yaml`, **Line No:** `4254`, **Line Pos:** `21` - **Line No:** `4254`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDisplays > items`

37. **File:** `en.yaml`, **Line No:** `4319`, **Line Pos:** `21` - **Line No:** `4319`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedTokenAuthMethods > items`

38. **File:** `en.yaml`, **Line No:** `4356`, **Line Pos:** `21` - **Line No:** `4356`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

39. **File:** `en.yaml`, **Line No:** `4383`, **Line Pos:** `21` - **Line No:** `4383`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

40. **File:** `en.yaml`, **Line No:** `4521`, **Line Pos:** `19` - **Line No:** `4521`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > accessTokenSignAlg`

41. **File:** `en.yaml`, **Line No:** `4671`, **Line Pos:** `21` - **Line No:** `4671`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimTypes > items`

42. **File:** `en.yaml`, **Line No:** `4883`, **Line Pos:** `21` - **Line No:** `4883`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

43. **File:** `en.yaml`, **Line No:** `4974`, **Line Pos:** `19` - **Line No:** `4974`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > userCodeCharset`

44. **File:** `en.yaml`, **Line No:** `5020`, **Line Pos:** `19` - **Line No:** `5020`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

45. **File:** `en.yaml`, **Line No:** `5440`, **Line Pos:** `21` - **Line No:** `5440`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAttachments > items`

46. **File:** `en.yaml`, **Line No:** `5512`, **Line Pos:** `21` - **Line No:** `5512`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

47. **File:** `en.yaml`, **Line No:** `5662`, **Line Pos:** `21` - **Line No:** `5662`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedPromptValues > items`

48. **File:** `en.yaml`, **Line No:** `5689`, **Line Pos:** `21` - **Line No:** `5689`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > fapiModes > items`

49. **File:** `en.yaml`, **Line No:** `5912`, **Line Pos:** `21` - **Line No:** `5912`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedGrantTypes > items`

50. **File:** `en.yaml`, **Line No:** `5933`, **Line Pos:** `21` - **Line No:** `5933`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedResponseTypes > items`

51. **File:** `en.yaml`, **Line No:** `5961`, **Line Pos:** `21` - **Line No:** `5961`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedServiceProfiles > items`

52. **File:** `en.yaml`, **Line No:** `6014`, **Line Pos:** `21` - **Line No:** `6014`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDisplays > items`

53. **File:** `en.yaml`, **Line No:** `6079`, **Line Pos:** `21` - **Line No:** `6079`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedTokenAuthMethods > items`

54. **File:** `en.yaml`, **Line No:** `6116`, **Line Pos:** `21` - **Line No:** `6116`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedRevocationAuthMethods > items`

55. **File:** `en.yaml`, **Line No:** `6143`, **Line Pos:** `21` - **Line No:** `6143`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedIntrospectionAuthMethods > items`

56. **File:** `en.yaml`, **Line No:** `6281`, **Line Pos:** `19` - **Line No:** `6281`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > accessTokenSignAlg`

57. **File:** `en.yaml`, **Line No:** `6431`, **Line Pos:** `21` - **Line No:** `6431`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClaimTypes > items`

58. **File:** `en.yaml`, **Line No:** `6643`, **Line Pos:** `21` - **Line No:** `6643`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedBackchannelTokenDeliveryModes > items`

59. **File:** `en.yaml`, **Line No:** `6734`, **Line Pos:** `19` - **Line No:** `6734`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > userCodeCharset`

60. **File:** `en.yaml`, **Line No:** `6780`, **Line Pos:** `19` - **Line No:** `6780`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > verifiedClaimsValidationSchemaSet`

61. **File:** `en.yaml`, **Line No:** `7200`, **Line Pos:** `21` - **Line No:** `7200`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedAttachments > items`

62. **File:** `en.yaml`, **Line No:** `7272`, **Line Pos:** `21` - **Line No:** `7272`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClientRegistrationTypes > items`

63. **File:** `en.yaml`, **Line No:** `7422`, **Line Pos:** `21` - **Line No:** `7422`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedPromptValues > items`

64. **File:** `en.yaml`, **Line No:** `7449`, **Line Pos:** `21` - **Line No:** `7449`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > fapiModes > items`

65. **File:** `en.yaml`, **Line No:** `7641`, **Line Pos:** `23` - **Line No:** `7641`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedGrantTypes > items`

66. **File:** `en.yaml`, **Line No:** `7662`, **Line Pos:** `23` - **Line No:** `7662`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

67. **File:** `en.yaml`, **Line No:** `7690`, **Line Pos:** `23` - **Line No:** `7690`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

68. **File:** `en.yaml`, **Line No:** `7743`, **Line Pos:** `23` - **Line No:** `7743`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDisplays > items`

69. **File:** `en.yaml`, **Line No:** `7808`, **Line Pos:** `23` - **Line No:** `7808`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods > items`

70. **File:** `en.yaml`, **Line No:** `7845`, **Line Pos:** `23` - **Line No:** `7845`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

71. **File:** `en.yaml`, **Line No:** `7872`, **Line Pos:** `23` - **Line No:** `7872`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

72. **File:** `en.yaml`, **Line No:** `8010`, **Line Pos:** `21` - **Line No:** `8010`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > accessTokenSignAlg`

73. **File:** `en.yaml`, **Line No:** `8160`, **Line Pos:** `23` - **Line No:** `8160`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

74. **File:** `en.yaml`, **Line No:** `8372`, **Line Pos:** `23` - **Line No:** `8372`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

75. **File:** `en.yaml`, **Line No:** `8463`, **Line Pos:** `21` - **Line No:** `8463`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > userCodeCharset`

76. **File:** `en.yaml`, **Line No:** `8509`, **Line Pos:** `21` - **Line No:** `8509`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

77. **File:** `en.yaml`, **Line No:** `8929`, **Line Pos:** `23` - **Line No:** `8929`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedAttachments > items`

78. **File:** `en.yaml`, **Line No:** `9001`, **Line Pos:** `23` - **Line No:** `9001`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

79. **File:** `en.yaml`, **Line No:** `9151`, **Line Pos:** `23` - **Line No:** `9151`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedPromptValues > items`

80. **File:** `en.yaml`, **Line No:** `9178`, **Line Pos:** `23` - **Line No:** `9178`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > fapiModes > items`

81. **File:** `en.yaml`, **Line No:** `9569`, **Line Pos:** `21` - **Line No:** `9569`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedGrantTypes > items`

82. **File:** `en.yaml`, **Line No:** `9590`, **Line Pos:** `21` - **Line No:** `9590`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedResponseTypes > items`

83. **File:** `en.yaml`, **Line No:** `9618`, **Line Pos:** `21` - **Line No:** `9618`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedServiceProfiles > items`

84. **File:** `en.yaml`, **Line No:** `9671`, **Line Pos:** `21` - **Line No:** `9671`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedDisplays > items`

85. **File:** `en.yaml`, **Line No:** `9736`, **Line Pos:** `21` - **Line No:** `9736`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedTokenAuthMethods > items`

86. **File:** `en.yaml`, **Line No:** `9773`, **Line Pos:** `21` - **Line No:** `9773`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

87. **File:** `en.yaml`, **Line No:** `9800`, **Line Pos:** `21` - **Line No:** `9800`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

88. **File:** `en.yaml`, **Line No:** `9938`, **Line Pos:** `19` - **Line No:** `9938`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > accessTokenSignAlg`

89. **File:** `en.yaml`, **Line No:** `10088`, **Line Pos:** `21` - **Line No:** `10088`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedClaimTypes > items`

90. **File:** `en.yaml`, **Line No:** `10300`, **Line Pos:** `21` - **Line No:** `10300`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

91. **File:** `en.yaml`, **Line No:** `10391`, **Line Pos:** `19` - **Line No:** `10391`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > userCodeCharset`

92. **File:** `en.yaml`, **Line No:** `10437`, **Line Pos:** `19` - **Line No:** `10437`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

93. **File:** `en.yaml`, **Line No:** `10857`, **Line Pos:** `21` - **Line No:** `10857`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedAttachments > items`

94. **File:** `en.yaml`, **Line No:** `10929`, **Line Pos:** `21` - **Line No:** `10929`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

95. **File:** `en.yaml`, **Line No:** `11079`, **Line Pos:** `21` - **Line No:** `11079`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > supportedPromptValues > items`

96. **File:** `en.yaml`, **Line No:** `11106`, **Line Pos:** `21` - **Line No:** `11106`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/json > schema > properties > fapiModes > items`

97. **File:** `en.yaml`, **Line No:** `11377`, **Line Pos:** `21` - **Line No:** `11377`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedGrantTypes > items`

98. **File:** `en.yaml`, **Line No:** `11398`, **Line Pos:** `21` - **Line No:** `11398`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedResponseTypes > items`

99. **File:** `en.yaml`, **Line No:** `11426`, **Line Pos:** `21` - **Line No:** `11426`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedServiceProfiles > items`

100. **File:** `en.yaml`, **Line No:** `11479`, **Line Pos:** `21` - **Line No:** `11479`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDisplays > items`

101. **File:** `en.yaml`, **Line No:** `11544`, **Line Pos:** `21` - **Line No:** `11544`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedTokenAuthMethods > items`

102. **File:** `en.yaml`, **Line No:** `11581`, **Line Pos:** `21` - **Line No:** `11581`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedRevocationAuthMethods > items`

103. **File:** `en.yaml`, **Line No:** `11608`, **Line Pos:** `21` - **Line No:** `11608`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedIntrospectionAuthMethods > items`

104. **File:** `en.yaml`, **Line No:** `11746`, **Line Pos:** `19` - **Line No:** `11746`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > accessTokenSignAlg`

105. **File:** `en.yaml`, **Line No:** `11896`, **Line Pos:** `21` - **Line No:** `11896`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClaimTypes > items`

106. **File:** `en.yaml`, **Line No:** `12108`, **Line Pos:** `21` - **Line No:** `12108`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedBackchannelTokenDeliveryModes > items`

107. **File:** `en.yaml`, **Line No:** `12199`, **Line Pos:** `19` - **Line No:** `12199`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > userCodeCharset`

108. **File:** `en.yaml`, **Line No:** `12245`, **Line Pos:** `19` - **Line No:** `12245`, **Line Pos:** `20`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > verifiedClaimsValidationSchemaSet`

109. **File:** `en.yaml`, **Line No:** `12665`, **Line Pos:** `21` - **Line No:** `12665`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedAttachments > items`

110. **File:** `en.yaml`, **Line No:** `12737`, **Line Pos:** `21` - **Line No:** `12737`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClientRegistrationTypes > items`

111. **File:** `en.yaml`, **Line No:** `12887`, **Line Pos:** `21` - **Line No:** `12887`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedPromptValues > items`

112. **File:** `en.yaml`, **Line No:** `12914`, **Line Pos:** `21` - **Line No:** `12914`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > fapiModes > items`

113. **File:** `en.yaml`, **Line No:** `13106`, **Line Pos:** `23` - **Line No:** `13106`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedGrantTypes > items`

114. **File:** `en.yaml`, **Line No:** `13127`, **Line Pos:** `23` - **Line No:** `13127`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

115. **File:** `en.yaml`, **Line No:** `13155`, **Line Pos:** `23` - **Line No:** `13155`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

116. **File:** `en.yaml`, **Line No:** `13208`, **Line Pos:** `23` - **Line No:** `13208`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedDisplays > items`

117. **File:** `en.yaml`, **Line No:** `13273`, **Line Pos:** `23` - **Line No:** `13273`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods > items`

118. **File:** `en.yaml`, **Line No:** `13310`, **Line Pos:** `23` - **Line No:** `13310`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

119. **File:** `en.yaml`, **Line No:** `13337`, **Line Pos:** `23` - **Line No:** `13337`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

120. **File:** `en.yaml`, **Line No:** `13475`, **Line Pos:** `21` - **Line No:** `13475`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > accessTokenSignAlg`

121. **File:** `en.yaml`, **Line No:** `13625`, **Line Pos:** `23` - **Line No:** `13625`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

122. **File:** `en.yaml`, **Line No:** `13837`, **Line Pos:** `23` - **Line No:** `13837`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

123. **File:** `en.yaml`, **Line No:** `13928`, **Line Pos:** `21` - **Line No:** `13928`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > userCodeCharset`

124. **File:** `en.yaml`, **Line No:** `13974`, **Line Pos:** `21` - **Line No:** `13974`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

125. **File:** `en.yaml`, **Line No:** `14394`, **Line Pos:** `23` - **Line No:** `14394`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedAttachments > items`

126. **File:** `en.yaml`, **Line No:** `14466`, **Line Pos:** `23` - **Line No:** `14466`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

127. **File:** `en.yaml`, **Line No:** `14616`, **Line Pos:** `23` - **Line No:** `14616`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > supportedPromptValues > items`

128. **File:** `en.yaml`, **Line No:** `14643`, **Line Pos:** `23` - **Line No:** `14643`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/update > post > responses > 200 > content > application/json > schema > properties > fapiModes > items`

129. **File:** `en.yaml`, **Line No:** `15137`, **Line Pos:** `21` - **Line No:** `15137`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > clientType`

130. **File:** `en.yaml`, **Line No:** `15145`, **Line Pos:** `21` - **Line No:** `15145`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > applicationType`

131. **File:** `en.yaml`, **Line No:** `15224`, **Line Pos:** `23` - **Line No:** `15224`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > grantTypes > items`

132. **File:** `en.yaml`, **Line No:** `15244`, **Line Pos:** `23` - **Line No:** `15244`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > responseTypes > items`

133. **File:** `en.yaml`, **Line No:** `15304`, **Line Pos:** `21` - **Line No:** `15304`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > authorizationSignAlg`

134. **File:** `en.yaml`, **Line No:** `15330`, **Line Pos:** `21` - **Line No:** `15330`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > authorizationEncryptionAlg`

135. **File:** `en.yaml`, **Line No:** `15358`, **Line Pos:** `21` - **Line No:** `15358`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > authorizationEncryptionEnc`

136. **File:** `en.yaml`, **Line No:** `15373`, **Line Pos:** `21` - **Line No:** `15373`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > tokenAuthMethod`

137. **File:** `en.yaml`, **Line No:** `15387`, **Line Pos:** `21` - **Line No:** `15387`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > tokenAuthSignAlg`

138. **File:** `en.yaml`, **Line No:** `15472`, **Line Pos:** `21` - **Line No:** `15472`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > requestSignAlg`

139. **File:** `en.yaml`, **Line No:** `15498`, **Line Pos:** `21` - **Line No:** `15498`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > requestEncryptionAlg`

140. **File:** `en.yaml`, **Line No:** `15526`, **Line Pos:** `21` - **Line No:** `15526`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > requestEncryptionEnc`

141. **File:** `en.yaml`, **Line No:** `15567`, **Line Pos:** `21` - **Line No:** `15567`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > idTokenSignAlg`

142. **File:** `en.yaml`, **Line No:** `15593`, **Line Pos:** `21` - **Line No:** `15593`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > idTokenEncryptionAlg`

143. **File:** `en.yaml`, **Line No:** `15621`, **Line Pos:** `21` - **Line No:** `15621`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > idTokenEncryptionEnc`

144. **File:** `en.yaml`, **Line No:** `15643`, **Line Pos:** `21` - **Line No:** `15643`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > subjectType`

145. **File:** `en.yaml`, **Line No:** `15702`, **Line Pos:** `21` - **Line No:** `15702`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > userInfoSignAlg`

146. **File:** `en.yaml`, **Line No:** `15728`, **Line Pos:** `21` - **Line No:** `15728`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > userInfoEncryptionAlg`

147. **File:** `en.yaml`, **Line No:** `15756`, **Line Pos:** `21` - **Line No:** `15756`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > userInfoEncryptionEnc`

148. **File:** `en.yaml`, **Line No:** `15860`, **Line Pos:** `21` - **Line No:** `15860`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > bcRequestSignAlg`

149. **File:** `en.yaml`, **Line No:** `16142`, **Line Pos:** `23` - **Line No:** `16142`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > clientRegistrationTypes > items`

150. **File:** `en.yaml`, **Line No:** `16201`, **Line Pos:** `23` - **Line No:** `16201`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > fapiModes > items`

151. **File:** `en.yaml`, **Line No:** `16223`, **Line Pos:** `23` - **Line No:** `16223`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/client/get/{clientId} > get > responses > 200 > content > application/json > schema > properties > responseModes > items`

152. **File:** `en.yaml`, **Line No:** `16522`, **Line Pos:** `27` - **Line No:** `16522`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > clientType`

153. **File:** `en.yaml`, **Line No:** `16530`, **Line Pos:** `27` - **Line No:** `16530`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/client/get/list > get > responses > 200 > content > application/json > schema > properties > clients > items > properties > applicationType`

154. **File:** `en_test.yaml`, **Line No:** `130`, **Line Pos:** `23` - **Line No:** `130`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedGrantTypes > items`

155. **File:** `en_test.yaml`, **Line No:** `151`, **Line Pos:** `23` - **Line No:** `151`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

156. **File:** `en_test.yaml`, **Line No:** `179`, **Line Pos:** `23` - **Line No:** `179`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

157. **File:** `en_test.yaml`, **Line No:** `232`, **Line Pos:** `23` - **Line No:** `232`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDisplays > items`

158. **File:** `en_test.yaml`, **Line No:** `297`, **Line Pos:** `23` - **Line No:** `297`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods > items`

159. **File:** `en_test.yaml`, **Line No:** `334`, **Line Pos:** `23` - **Line No:** `334`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

160. **File:** `en_test.yaml`, **Line No:** `361`, **Line Pos:** `23` - **Line No:** `361`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

161. **File:** `en_test.yaml`, **Line No:** `499`, **Line Pos:** `21` - **Line No:** `499`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenSignAlg`

162. **File:** `en_test.yaml`, **Line No:** `649`, **Line Pos:** `23` - **Line No:** `649`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

163. **File:** `en_test.yaml`, **Line No:** `861`, **Line Pos:** `23` - **Line No:** `861`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

164. **File:** `en_test.yaml`, **Line No:** `952`, **Line Pos:** `21` - **Line No:** `952`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userCodeCharset`

165. **File:** `en_test.yaml`, **Line No:** `998`, **Line Pos:** `21` - **Line No:** `998`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

166. **File:** `en_test.yaml`, **Line No:** `1418`, **Line Pos:** `23` - **Line No:** `1418`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAttachments > items`

167. **File:** `en_test.yaml`, **Line No:** `1490`, **Line Pos:** `23` - **Line No:** `1490`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

168. **File:** `en_test.yaml`, **Line No:** `1640`, **Line Pos:** `23` - **Line No:** `1640`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedPromptValues > items`

169. **File:** `en_test.yaml`, **Line No:** `1667`, **Line Pos:** `23` - **Line No:** `1667`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > fapiModes > items`

170. **File:** `en_test.yaml`, **Line No:** `2100`, **Line Pos:** `29` - **Line No:** `2100`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedGrantTypes > items`

171. **File:** `en_test.yaml`, **Line No:** `2121`, **Line Pos:** `29` - **Line No:** `2121`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedResponseTypes > items`

172. **File:** `en_test.yaml`, **Line No:** `2149`, **Line Pos:** `29` - **Line No:** `2149`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedServiceProfiles > items`

173. **File:** `en_test.yaml`, **Line No:** `2202`, **Line Pos:** `29` - **Line No:** `2202`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDisplays > items`

174. **File:** `en_test.yaml`, **Line No:** `2267`, **Line Pos:** `29` - **Line No:** `2267`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTokenAuthMethods > items`

175. **File:** `en_test.yaml`, **Line No:** `2304`, **Line Pos:** `29` - **Line No:** `2304`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedRevocationAuthMethods > items`

176. **File:** `en_test.yaml`, **Line No:** `2331`, **Line Pos:** `29` - **Line No:** `2331`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIntrospectionAuthMethods > items`

177. **File:** `en_test.yaml`, **Line No:** `2469`, **Line Pos:** `27` - **Line No:** `2469`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenSignAlg`

178. **File:** `en_test.yaml`, **Line No:** `2619`, **Line Pos:** `29` - **Line No:** `2619`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimTypes > items`

179. **File:** `en_test.yaml`, **Line No:** `2831`, **Line Pos:** `29` - **Line No:** `2831`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedBackchannelTokenDeliveryModes > items`

180. **File:** `en_test.yaml`, **Line No:** `2922`, **Line Pos:** `27` - **Line No:** `2922`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userCodeCharset`

181. **File:** `en_test.yaml`, **Line No:** `2968`, **Line Pos:** `27` - **Line No:** `2968`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > verifiedClaimsValidationSchemaSet`

182. **File:** `en_test.yaml`, **Line No:** `3388`, **Line Pos:** `29` - **Line No:** `3388`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAttachments > items`

183. **File:** `en_test.yaml`, **Line No:** `3460`, **Line Pos:** `29` - **Line No:** `3460`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClientRegistrationTypes > items`

184. **File:** `en_test.yaml`, **Line No:** `3610`, **Line Pos:** `29` - **Line No:** `3610`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedPromptValues > items`

185. **File:** `en_test.yaml`, **Line No:** `3637`, **Line Pos:** `29` - **Line No:** `3637`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > fapiModes > items`

186. **File:** `en_test.yaml`, **Line No:** `4036`, **Line Pos:** `21` - **Line No:** `4036`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedGrantTypes > items`

187. **File:** `en_test.yaml`, **Line No:** `4057`, **Line Pos:** `21` - **Line No:** `4057`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedResponseTypes > items`

188. **File:** `en_test.yaml`, **Line No:** `4085`, **Line Pos:** `21` - **Line No:** `4085`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedServiceProfiles > items`

189. **File:** `en_test.yaml`, **Line No:** `4138`, **Line Pos:** `21` - **Line No:** `4138`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDisplays > items`

190. **File:** `en_test.yaml`, **Line No:** `4203`, **Line Pos:** `21` - **Line No:** `4203`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedTokenAuthMethods > items`

191. **File:** `en_test.yaml`, **Line No:** `4240`, **Line Pos:** `21` - **Line No:** `4240`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

192. **File:** `en_test.yaml`, **Line No:** `4267`, **Line Pos:** `21` - **Line No:** `4267`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

193. **File:** `en_test.yaml`, **Line No:** `4405`, **Line Pos:** `19` - **Line No:** `4405`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > accessTokenSignAlg`

194. **File:** `en_test.yaml`, **Line No:** `4555`, **Line Pos:** `21` - **Line No:** `4555`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimTypes > items`

195. **File:** `en_test.yaml`, **Line No:** `4767`, **Line Pos:** `21` - **Line No:** `4767`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

196. **File:** `en_test.yaml`, **Line No:** `4858`, **Line Pos:** `19` - **Line No:** `4858`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > userCodeCharset`

197. **File:** `en_test.yaml`, **Line No:** `4904`, **Line Pos:** `19` - **Line No:** `4904`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

198. **File:** `en_test.yaml`, **Line No:** `5324`, **Line Pos:** `21` - **Line No:** `5324`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAttachments > items`

199. **File:** `en_test.yaml`, **Line No:** `5396`, **Line Pos:** `21` - **Line No:** `5396`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

200. **File:** `en_test.yaml`, **Line No:** `5546`, **Line Pos:** `21` - **Line No:** `5546`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedPromptValues > items`

201. **File:** `en_test.yaml`, **Line No:** `5573`, **Line Pos:** `21` - **Line No:** `5573`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > fapiModes > items`

202. **File:** `en_test.yaml`, **Line No:** `5796`, **Line Pos:** `21` - **Line No:** `5796`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedGrantTypes > items`

203. **File:** `en_test.yaml`, **Line No:** `5817`, **Line Pos:** `21` - **Line No:** `5817`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedResponseTypes > items`

204. **File:** `en_test.yaml`, **Line No:** `5845`, **Line Pos:** `21` - **Line No:** `5845`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedServiceProfiles > items`

205. **File:** `en_test.yaml`, **Line No:** `5898`, **Line Pos:** `21` - **Line No:** `5898`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDisplays > items`

206. **File:** `en_test.yaml`, **Line No:** `5963`, **Line Pos:** `21` - **Line No:** `5963`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedTokenAuthMethods > items`

207. **File:** `en_test.yaml`, **Line No:** `6000`, **Line Pos:** `21` - **Line No:** `6000`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedRevocationAuthMethods > items`

208. **File:** `en_test.yaml`, **Line No:** `6027`, **Line Pos:** `21` - **Line No:** `6027`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedIntrospectionAuthMethods > items`

209. **File:** `en_test.yaml`, **Line No:** `6165`, **Line Pos:** `19` - **Line No:** `6165`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > accessTokenSignAlg`

210. **File:** `en_test.yaml`, **Line No:** `6315`, **Line Pos:** `21` - **Line No:** `6315`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClaimTypes > items`

211. **File:** `en_test.yaml`, **Line No:** `6527`, **Line Pos:** `21` - **Line No:** `6527`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedBackchannelTokenDeliveryModes > items`

212. **File:** `en_test.yaml`, **Line No:** `6618`, **Line Pos:** `19` - **Line No:** `6618`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > userCodeCharset`

213. **File:** `en_test.yaml`, **Line No:** `6664`, **Line Pos:** `19` - **Line No:** `6664`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > verifiedClaimsValidationSchemaSet`

214. **File:** `en_test.yaml`, **Line No:** `7084`, **Line Pos:** `21` - **Line No:** `7084`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedAttachments > items`

215. **File:** `en_test.yaml`, **Line No:** `7156`, **Line Pos:** `21` - **Line No:** `7156`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClientRegistrationTypes > items`

216. **File:** `en_test.yaml`, **Line No:** `7306`, **Line Pos:** `21` - **Line No:** `7306`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedPromptValues > items`

217. **File:** `en_test.yaml`, **Line No:** `7333`, **Line Pos:** `21` - **Line No:** `7333`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > fapiModes > items`

218. **File:** `en_test.yaml`, **Line No:** `7525`, **Line Pos:** `23` - **Line No:** `7525`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedGrantTypes > items`

219. **File:** `en_test.yaml`, **Line No:** `7546`, **Line Pos:** `23` - **Line No:** `7546`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

220. **File:** `en_test.yaml`, **Line No:** `7574`, **Line Pos:** `23` - **Line No:** `7574`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

221. **File:** `en_test.yaml`, **Line No:** `7627`, **Line Pos:** `23` - **Line No:** `7627`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDisplays > items`

222. **File:** `en_test.yaml`, **Line No:** `7692`, **Line Pos:** `23` - **Line No:** `7692`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods > items`

223. **File:** `en_test.yaml`, **Line No:** `7729`, **Line Pos:** `23` - **Line No:** `7729`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

224. **File:** `en_test.yaml`, **Line No:** `7756`, **Line Pos:** `23` - **Line No:** `7756`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

225. **File:** `en_test.yaml`, **Line No:** `7894`, **Line Pos:** `21` - **Line No:** `7894`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > accessTokenSignAlg`

226. **File:** `en_test.yaml`, **Line No:** `8044`, **Line Pos:** `23` - **Line No:** `8044`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

227. **File:** `en_test.yaml`, **Line No:** `8256`, **Line Pos:** `23` - **Line No:** `8256`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

228. **File:** `en_test.yaml`, **Line No:** `8347`, **Line Pos:** `21` - **Line No:** `8347`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > userCodeCharset`

229. **File:** `en_test.yaml`, **Line No:** `8393`, **Line Pos:** `21` - **Line No:** `8393`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

230. **File:** `en_test.yaml`, **Line No:** `8813`, **Line Pos:** `23` - **Line No:** `8813`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedAttachments > items`

231. **File:** `en_test.yaml`, **Line No:** `8885`, **Line Pos:** `23` - **Line No:** `8885`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

232. **File:** `en_test.yaml`, **Line No:** `9035`, **Line Pos:** `23` - **Line No:** `9035`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedPromptValues > items`

233. **File:** `en_test.yaml`, **Line No:** `9062`, **Line Pos:** `23` - **Line No:** `9062`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > fapiModes > items`

234. **File:** `en_test.yaml`, **Line No:** `9379`, **Line Pos:** `11` - **Line No:** `9379`, **Line Pos:** `12`, **Path:** `# > components > schemas > AccessToken > properties > grantType`


### <a id="warn-issue-no-7---schema-object-description-contains-leadingtrailing-white-space-characters-15"></a> `Warn` Issue No. 7 - Schema object description contains leading/trailing white-space characters. (15)

| Property | Value |
| -------- | ----- |
| Rule Id | `no-trailing-leading-spaces-in-schema-description` |
| Ruleset Id | `openapi-v3-docsgen-syntax-linting` |
| Type of Issue | Syntax |
| Broad Category of Issue | OpenAPI Schemas |
| Possible Impact On Output Of | `Developer Experience Portal` |

Description of Schema Object should not contain any leading or trailing white-space characters.

#### <a id="tips-7"></a> Tips

* Remove all leading or trailing white-space characters such as spaces, tabs, or line breaks.

#### <a id="for-more-information-7"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schema-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-15"></a> Affected Components (`15`)

1. **File:** `en_test.yaml`, **Line No:** `330`, **Line Pos:** `34` - **Line No:** `330`, **Line Pos:** `189`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directRevocationEndpointEnabled > description`

2. **File:** `en_test.yaml`, **Line No:** `355`, **Line Pos:** `34` - **Line No:** `355`, **Line Pos:** `186`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directIntrospectionEndpointEnabled > description`

3. **File:** `en_test.yaml`, **Line No:** `573`, **Line Pos:** `40` - **Line No:** `573`, **Line Pos:** `228`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > defaultEntry > description`

4. **File:** `en_test.yaml`, **Line No:** `2300`, **Line Pos:** `40` - **Line No:** `2300`, **Line Pos:** `195`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directRevocationEndpointEnabled > description`

5. **File:** `en_test.yaml`, **Line No:** `2325`, **Line Pos:** `40` - **Line No:** `2325`, **Line Pos:** `192`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directIntrospectionEndpointEnabled > description`

6. **File:** `en_test.yaml`, **Line No:** `2543`, **Line Pos:** `46` - **Line No:** `2543`, **Line Pos:** `234`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > defaultEntry > description`

7. **File:** `en_test.yaml`, **Line No:** `4236`, **Line Pos:** `32` - **Line No:** `4236`, **Line Pos:** `187`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directRevocationEndpointEnabled > description`

8. **File:** `en_test.yaml`, **Line No:** `4261`, **Line Pos:** `32` - **Line No:** `4261`, **Line Pos:** `184`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directIntrospectionEndpointEnabled > description`

9. **File:** `en_test.yaml`, **Line No:** `4479`, **Line Pos:** `38` - **Line No:** `4479`, **Line Pos:** `226`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > defaultEntry > description`

10. **File:** `en_test.yaml`, **Line No:** `5996`, **Line Pos:** `32` - **Line No:** `5996`, **Line Pos:** `187`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > directRevocationEndpointEnabled > description`

11. **File:** `en_test.yaml`, **Line No:** `6021`, **Line Pos:** `32` - **Line No:** `6021`, **Line Pos:** `184`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > directIntrospectionEndpointEnabled > description`

12. **File:** `en_test.yaml`, **Line No:** `6239`, **Line Pos:** `38` - **Line No:** `6239`, **Line Pos:** `226`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > defaultEntry > description`

13. **File:** `en_test.yaml`, **Line No:** `7725`, **Line Pos:** `34` - **Line No:** `7725`, **Line Pos:** `189`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > directRevocationEndpointEnabled > description`

14. **File:** `en_test.yaml`, **Line No:** `7750`, **Line Pos:** `34` - **Line No:** `7750`, **Line Pos:** `186`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > directIntrospectionEndpointEnabled > description`

15. **File:** `en_test.yaml`, **Line No:** `7968`, **Line Pos:** `40` - **Line No:** `7968`, **Line Pos:** `228`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > defaultEntry > description`


### <a id="warn-issue-no-8---unsupported-extension-detected-3"></a> `Warn` Issue No. 8 - Unsupported extension detected. (3)

| Property | Value |
| -------- | ----- |
| Rule Id | `supported-vendor-extension` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Vendor Extensions |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

APIMatic supports certain vendor extensions which are loaded at the time of importing API description files containing these extensions. These include APIMatic specific extensions as well that are used for configuring products like Code Generation, Transformer, etc. All other extensions will be ignored or may not work as expected.

#### <a id="tips-8"></a> Tips

* Remove unsupported vendor extensions from your API description file.
* Contact APIMatic team to know more about whether a specific vendor extension is supported or not. In some cases, we may decide to support the vendor extension if its importance is established.

#### <a id="for-more-information-8"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#specification-extensions
* https://docs.apimatic.io/specification-extensions/spec-extensions-overview/
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-3"></a> Affected Components (`3`)

1. **File:** `en_test.yaml`, **Line No:** `1923`, **Line Pos:** `7` - **Line No:** `1923`, **Line Pos:** `21`, **Path:** `# > paths > /api/{serviceId}/service/get > get`
    * _**Unsupported Extension:**_ x-code-samples

2. **File:** `en_test.yaml`, **Line No:** `3903`, **Line Pos:** `7` - **Line No:** `3903`, **Line Pos:** `21`, **Path:** `# > paths > /api/service/get/list > get`
    * _**Unsupported Extension:**_ x-code-samples

3. **File:** `en_test.yaml`, **Line No:** `9309`, **Line Pos:** `7` - **Line No:** `9309`, **Line Pos:** `21`, **Path:** `# > paths > /api/service/create > post`
    * _**Unsupported Extension:**_ x-code-samples


### <a id="warn-issue-no-9---component-was-defined-but-never-used-3"></a> `Warn` Issue No. 9 - Component was defined but never used. (3)

| Property | Value |
| -------- | ----- |
| Rule Id | `at-least-one-component-reference` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Components |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

A component that is defined globally using the 'components' root object property must be referenced at least once by any other object in the API specification document. Referencing is performed using $ref.

#### <a id="tips-9"></a> Tips

* Ensure that each globally defined component is referenced at least once in the API.
* A component can be referenced using $ref with a valid path that can begin with '#/components/'.
* If a schema 'Pet' is defined under #/components/schemas, there must exist an object in the document that references this schema using a path like #/components/schemas/Pet.
* The components section helps define reusable components. If a component definition is not expected to be used, it must be removed.

#### <a id="for-more-information-9"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#components-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-3-1"></a> Affected Components (`3`)

1. **File:** `en_test.yaml`, **Line No:** `9342`, **Line Pos:** `5` - **Line No:** `9342`, **Line Pos:** `16`, **Path:** `# > components > schemas`
    * _**Unused Component Name:**_ AccessToken

2. **File:** `en_test.yaml`, **Line No:** `9422`, **Line Pos:** `5` - **Line No:** `9422`, **Line Pos:** `20`, **Path:** `# > components > schemas`
    * _**Unused Component Name:**_ ApplicationType

3. **File:** `en_test.yaml`, **Line No:** `9430`, **Line Pos:** `5` - **Line No:** `9430`, **Line Pos:** `25`, **Path:** `# > components > schemas`
    * _**Unused Component Name:**_ AuthorizationDetails


### <a id="warn-issue-no-10---undefined-tag-used-in-operation-object-3"></a> `Warn` Issue No. 10 - Undefined tag used in operation object. (3)

| Property | Value |
| -------- | ----- |
| Rule Id | `pre-defined-operation-tag-in-global-tags` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Operations |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

Each tag used in the API must be defined in the root level tags list of the API specification. This ensures that all tags used in the API are properly defined, which helps with documentation generation and other tooling. Please check the root level tags list and ensure that all tags used in the API are properly defined.

#### <a id="tips-10"></a> Tips

* Ensure that the tag used in the operation is defined in the root level tags list of the API specification.
* Check the spelling and capitalization of the tag used in the operation.
* If the tag used in the operation is not defined in the root level tags list, add it to the list and ensure that it is properly formatted.
* Verify that there are no typos or syntax errors in the API specification.

#### <a id="for-more-information-10"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#fixed-fields-8
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-3-2"></a> Affected Components (`3`)

1. **File:** `en_test.yaml`, **Line No:** `1947`, **Line Pos:** `11` - **Line No:** `1947`, **Line Pos:** `29`, **Path:** `# > paths > /api/{serviceId}/service/get > get > tags > 0`
    * _**Undefined Tag:**_ Service Management

2. **File:** `en_test.yaml`, **Line No:** `3929`, **Line Pos:** `11` - **Line No:** `3929`, **Line Pos:** `29`, **Path:** `# > paths > /api/service/get/list > get > tags > 0`
    * _**Undefined Tag:**_ Service Management

3. **File:** `en_test.yaml`, **Line No:** `9339`, **Line Pos:** `11` - **Line No:** `9339`, **Line Pos:** `29`, **Path:** `# > paths > /api/service/create > post > tags > 0`
    * _**Undefined Tag:**_ Service Management


### <a id="warn-issue-no-11---no-security-mechanism-applied-to-the-api-1"></a> `Warn` Issue No. 11 - No security mechanism applied to the API. (1)

| Property | Value |
| -------- | ----- |
| Rule Id | `at-least-one-security-mechanism-applied` |
| Ruleset Id | `openapi-v3-apimatic-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Security Requirements |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

APIs that require some form of authentication must define the security schemes used, in the global Components Object using the `securitySchemes` property and apply these security schemes to the endpoints that require authentication. This will ensure that the requests that require authentication are authenticated properly.

#### <a id="tips-11"></a> Tips

* Remove any Authorization header definitions from the operations and instead define the authentication mechanism using the OpenAPI's global security schemes. Then apply those schemes to operations as required.
* When defining a security scheme globally assign a short but unique name for it.
* Choose the appropriate security scheme type when defining a security scheme.
* If your API does not require authentication, you can ignore this lint check or disable it.

#### <a id="for-more-information-11"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#components-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#security-scheme-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-1-2"></a> Affected Components (`1`)

1. **File:** `en_test.yaml`, **Line No:** `9341`, **Line Pos:** `3` - **Line No:** `9341`, **Line Pos:** `4`, **Path:** `# > components`


### <a id="info-issue-no-12---the-root-openapi-file-name-does-not-follow-recommended-conventions-1"></a> `Info` Issue No. 12 - The root OpenAPI file name does not follow recommended conventions. (1)

| Property | Value |
| -------- | ----- |
| Rule Id | `valid-openapi-file-naming-conventions` |
| Ruleset Id | `openapi-v3-standards-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Root Information |
| Possible Impact On Output Of | `API Transformer`, `Code Generation`, `Developer Experience Portal` |

The root OpenAPI document is recommended to be named as either `openapi.json` or `openapi.yaml` depending upon the data format used in the file.

#### <a id="tips-12"></a> Tips

* Main or root OpenAPI file is one which contains the OpenAPI version, paths and other information.
* Standardized naming of files helps improve their discoverability for your users.

#### <a id="for-more-information-12"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#document-structure
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#document-structure
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-1-3"></a> Affected Components (`1`)

1. **File:** `en_test.yaml`, **Line No:** `1`, **Line Pos:** `1` - **Line No:** `1`, **Line Pos:** `2`, **Path:** `#`
    * _**Current File Name:**_ en_test.yaml


### <a id="info-issue-no-13---schema-object-description-is-missing-222"></a> `Info` Issue No. 13 - Schema object description is missing. (222)

| Property | Value |
| -------- | ----- |
| Rule Id | `schema-description-exists` |
| Ruleset Id | `openapi-v3-docsgen-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Schemas |
| Possible Impact On Output Of | `Developer Experience Portal` |

The Schema Object must specify details about the schema or the type of data it represents, using the `description` property. The value of the description must be non-null and non-empty.

#### <a id="tips-13"></a> Tips

* Ensure that the Schema Object contains the `description` property.
* Ensure that Schema Object description value is not null or empty.

#### <a id="for-more-information-13"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schema-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-222"></a> Affected Components (`222`)

1. **File:** `en_test.yaml`, **Line No:** `34`, **Line Pos:** `17` - **Line No:** `34`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema`

2. **File:** `en_test.yaml`, **Line No:** `67`, **Line Pos:** `23` - **Line No:** `67`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata > items`

3. **File:** `en_test.yaml`, **Line No:** `121`, **Line Pos:** `23` - **Line No:** `121`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAcrs > items`

4. **File:** `en_test.yaml`, **Line No:** `151`, **Line Pos:** `23` - **Line No:** `151`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

5. **File:** `en_test.yaml`, **Line No:** `170`, **Line Pos:** `23` - **Line No:** `170`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAuthorizationDetailsTypes > items`

6. **File:** `en_test.yaml`, **Line No:** `179`, **Line Pos:** `23` - **Line No:** `179`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

7. **File:** `en_test.yaml`, **Line No:** `222`, **Line Pos:** `23` - **Line No:** `222`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedUiLocales > items`

8. **File:** `en_test.yaml`, **Line No:** `440`, **Line Pos:** `23` - **Line No:** `440`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustedRootCertificates > items`

9. **File:** `en_test.yaml`, **Line No:** `446`, **Line Pos:** `23` - **Line No:** `446`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

10. **File:** `en_test.yaml`, **Line No:** `449`, **Line Pos:** `27` - **Line No:** `449`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > name`

11. **File:** `en_test.yaml`, **Line No:** `451`, **Line Pos:** `27` - **Line No:** `451`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > uri`

12. **File:** `en_test.yaml`, **Line No:** `566`, **Line Pos:** `23` - **Line No:** `566`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

13. **File:** `en_test.yaml`, **Line No:** `581`, **Line Pos:** `29` - **Line No:** `581`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

14. **File:** `en_test.yaml`, **Line No:** `593`, **Line Pos:** `29` - **Line No:** `593`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

15. **File:** `en_test.yaml`, **Line No:** `649`, **Line Pos:** `23` - **Line No:** `649`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

16. **File:** `en_test.yaml`, **Line No:** `663`, **Line Pos:** `23` - **Line No:** `663`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimLocales > items`

17. **File:** `en_test.yaml`, **Line No:** `674`, **Line Pos:** `23` - **Line No:** `674`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaims > items`

18. **File:** `en_test.yaml`, **Line No:** `861`, **Line Pos:** `23` - **Line No:** `861`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

19. **File:** `en_test.yaml`, **Line No:** `966`, **Line Pos:** `23` - **Line No:** `966`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTrustFrameworks > items`

20. **File:** `en_test.yaml`, **Line No:** `973`, **Line Pos:** `23` - **Line No:** `973`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedEvidence > items`

21. **File:** `en_test.yaml`, **Line No:** `979`, **Line Pos:** `23` - **Line No:** `979`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIdentityDocuments > items`

22. **File:** `en_test.yaml`, **Line No:** `986`, **Line Pos:** `23` - **Line No:** `986`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedVerificationMethods > items`

23. **File:** `en_test.yaml`, **Line No:** `993`, **Line Pos:** `23` - **Line No:** `993`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedVerifiedClaims > items`

24. **File:** `en_test.yaml`, **Line No:** `1007`, **Line Pos:** `23` - **Line No:** `1007`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes > items`

25. **File:** `en_test.yaml`, **Line No:** `1060`, **Line Pos:** `23` - **Line No:** `1060`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedCustomClientMetadata > items`

26. **File:** `en_test.yaml`, **Line No:** `1359`, **Line Pos:** `23` - **Line No:** `1359`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authorityHints > items`

27. **File:** `en_test.yaml`, **Line No:** `1433`, **Line Pos:** `23` - **Line No:** `1433`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDigestAlgorithms > items`

28. **File:** `en_test.yaml`, **Line No:** `1443`, **Line Pos:** `23` - **Line No:** `1443`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocuments > items`

29. **File:** `en_test.yaml`, **Line No:** `1450`, **Line Pos:** `23` - **Line No:** `1450`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsMethods > items`

30. **File:** `en_test.yaml`, **Line No:** `1463`, **Line Pos:** `23` - **Line No:** `1463`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsValidationMethods > items`

31. **File:** `en_test.yaml`, **Line No:** `1472`, **Line Pos:** `23` - **Line No:** `1472`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsVerificationMethods > items`

32. **File:** `en_test.yaml`, **Line No:** `1481`, **Line Pos:** `23` - **Line No:** `1481`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedElectronicRecords > items`

33. **File:** `en_test.yaml`, **Line No:** `1488`, **Line Pos:** `21` - **Line No:** `1488`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes`

34. **File:** `en_test.yaml`, **Line No:** `1548`, **Line Pos:** `23` - **Line No:** `1548`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

35. **File:** `en_test.yaml`, **Line No:** `1574`, **Line Pos:** `23` - **Line No:** `1574`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsCheckMethods > items`

36. **File:** `en_test.yaml`, **Line No:** `1667`, **Line Pos:** `23` - **Line No:** `1667`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > fapiModes > items`

37. **File:** `en_test.yaml`, **Line No:** `1691`, **Line Pos:** `21` - **Line No:** `1691`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

38. **File:** `en_test.yaml`, **Line No:** `1696`, **Line Pos:** `27` - **Line No:** `1696`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > authorizationServers > items`

39. **File:** `en_test.yaml`, **Line No:** `1720`, **Line Pos:** `27` - **Line No:** `1720`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

40. **File:** `en_test.yaml`, **Line No:** `1727`, **Line Pos:** `27` - **Line No:** `1727`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

41. **File:** `en_test.yaml`, **Line No:** `1863`, **Line Pos:** `17` - **Line No:** `1863`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 400 > content > application/json > schema`

42. **File:** `en_test.yaml`, **Line No:** `1879`, **Line Pos:** `17` - **Line No:** `1879`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 401 > content > application/json > schema`

43. **File:** `en_test.yaml`, **Line No:** `1895`, **Line Pos:** `17` - **Line No:** `1895`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 403 > content > application/json > schema`

44. **File:** `en_test.yaml`, **Line No:** `1911`, **Line Pos:** `17` - **Line No:** `1911`, **Line Pos:** `18`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 500 > content > application/json > schema`

45. **File:** `en_test.yaml`, **Line No:** `1981`, **Line Pos:** `17` - **Line No:** `1981`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema`

46. **File:** `en_test.yaml`, **Line No:** `2004`, **Line Pos:** `23` - **Line No:** `2004`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items`

47. **File:** `en_test.yaml`, **Line No:** `2037`, **Line Pos:** `29` - **Line No:** `2037`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata > items`

48. **File:** `en_test.yaml`, **Line No:** `2091`, **Line Pos:** `29` - **Line No:** `2091`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAcrs > items`

49. **File:** `en_test.yaml`, **Line No:** `2121`, **Line Pos:** `29` - **Line No:** `2121`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedResponseTypes > items`

50. **File:** `en_test.yaml`, **Line No:** `2140`, **Line Pos:** `29` - **Line No:** `2140`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAuthorizationDetailsTypes > items`

51. **File:** `en_test.yaml`, **Line No:** `2149`, **Line Pos:** `29` - **Line No:** `2149`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedServiceProfiles > items`

52. **File:** `en_test.yaml`, **Line No:** `2192`, **Line Pos:** `29` - **Line No:** `2192`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedUiLocales > items`

53. **File:** `en_test.yaml`, **Line No:** `2410`, **Line Pos:** `29` - **Line No:** `2410`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustedRootCertificates > items`

54. **File:** `en_test.yaml`, **Line No:** `2416`, **Line Pos:** `29` - **Line No:** `2416`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items`

55. **File:** `en_test.yaml`, **Line No:** `2419`, **Line Pos:** `33` - **Line No:** `2419`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items > properties > name`

56. **File:** `en_test.yaml`, **Line No:** `2421`, **Line Pos:** `33` - **Line No:** `2421`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items > properties > uri`

57. **File:** `en_test.yaml`, **Line No:** `2536`, **Line Pos:** `29` - **Line No:** `2536`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items`

58. **File:** `en_test.yaml`, **Line No:** `2551`, **Line Pos:** `35` - **Line No:** `2551`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions > items`

59. **File:** `en_test.yaml`, **Line No:** `2563`, **Line Pos:** `35` - **Line No:** `2563`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes > items`

60. **File:** `en_test.yaml`, **Line No:** `2619`, **Line Pos:** `29` - **Line No:** `2619`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimTypes > items`

61. **File:** `en_test.yaml`, **Line No:** `2633`, **Line Pos:** `29` - **Line No:** `2633`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimLocales > items`

62. **File:** `en_test.yaml`, **Line No:** `2644`, **Line Pos:** `29` - **Line No:** `2644`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaims > items`

63. **File:** `en_test.yaml`, **Line No:** `2831`, **Line Pos:** `29` - **Line No:** `2831`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedBackchannelTokenDeliveryModes > items`

64. **File:** `en_test.yaml`, **Line No:** `2936`, **Line Pos:** `29` - **Line No:** `2936`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTrustFrameworks > items`

65. **File:** `en_test.yaml`, **Line No:** `2943`, **Line Pos:** `29` - **Line No:** `2943`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedEvidence > items`

66. **File:** `en_test.yaml`, **Line No:** `2949`, **Line Pos:** `29` - **Line No:** `2949`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIdentityDocuments > items`

67. **File:** `en_test.yaml`, **Line No:** `2956`, **Line Pos:** `29` - **Line No:** `2956`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedVerificationMethods > items`

68. **File:** `en_test.yaml`, **Line No:** `2963`, **Line Pos:** `29` - **Line No:** `2963`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedVerifiedClaims > items`

69. **File:** `en_test.yaml`, **Line No:** `2977`, **Line Pos:** `29` - **Line No:** `2977`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes > items`

70. **File:** `en_test.yaml`, **Line No:** `3030`, **Line Pos:** `29` - **Line No:** `3030`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedCustomClientMetadata > items`

71. **File:** `en_test.yaml`, **Line No:** `3329`, **Line Pos:** `29` - **Line No:** `3329`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authorityHints > items`

72. **File:** `en_test.yaml`, **Line No:** `3403`, **Line Pos:** `29` - **Line No:** `3403`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDigestAlgorithms > items`

73. **File:** `en_test.yaml`, **Line No:** `3413`, **Line Pos:** `29` - **Line No:** `3413`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocuments > items`

74. **File:** `en_test.yaml`, **Line No:** `3420`, **Line Pos:** `29` - **Line No:** `3420`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsMethods > items`

75. **File:** `en_test.yaml`, **Line No:** `3433`, **Line Pos:** `29` - **Line No:** `3433`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsValidationMethods > items`

76. **File:** `en_test.yaml`, **Line No:** `3442`, **Line Pos:** `29` - **Line No:** `3442`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsVerificationMethods > items`

77. **File:** `en_test.yaml`, **Line No:** `3451`, **Line Pos:** `29` - **Line No:** `3451`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedElectronicRecords > items`

78. **File:** `en_test.yaml`, **Line No:** `3458`, **Line Pos:** `27` - **Line No:** `3458`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClientRegistrationTypes`

79. **File:** `en_test.yaml`, **Line No:** `3518`, **Line Pos:** `29` - **Line No:** `3518`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors > items`

80. **File:** `en_test.yaml`, **Line No:** `3544`, **Line Pos:** `29` - **Line No:** `3544`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsCheckMethods > items`

81. **File:** `en_test.yaml`, **Line No:** `3637`, **Line Pos:** `29` - **Line No:** `3637`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > fapiModes > items`

82. **File:** `en_test.yaml`, **Line No:** `3661`, **Line Pos:** `27` - **Line No:** `3661`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata`

83. **File:** `en_test.yaml`, **Line No:** `3666`, **Line Pos:** `33` - **Line No:** `3666`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > authorizationServers > items`

84. **File:** `en_test.yaml`, **Line No:** `3690`, **Line Pos:** `33` - **Line No:** `3690`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

85. **File:** `en_test.yaml`, **Line No:** `3697`, **Line Pos:** `33` - **Line No:** `3697`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

86. **File:** `en_test.yaml`, **Line No:** `3843`, **Line Pos:** `17` - **Line No:** `3843`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 400 > content > application/json > schema`

87. **File:** `en_test.yaml`, **Line No:** `3859`, **Line Pos:** `17` - **Line No:** `3859`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 401 > content > application/json > schema`

88. **File:** `en_test.yaml`, **Line No:** `3875`, **Line Pos:** `17` - **Line No:** `3875`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 403 > content > application/json > schema`

89. **File:** `en_test.yaml`, **Line No:** `3891`, **Line Pos:** `17` - **Line No:** `3891`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/get/list > get > responses > 500 > content > application/json > schema`

90. **File:** `en_test.yaml`, **Line No:** `3940`, **Line Pos:** `15` - **Line No:** `3940`, **Line Pos:** `16`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema`

91. **File:** `en_test.yaml`, **Line No:** `3973`, **Line Pos:** `21` - **Line No:** `3973`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata > items`

92. **File:** `en_test.yaml`, **Line No:** `4027`, **Line Pos:** `21` - **Line No:** `4027`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAcrs > items`

93. **File:** `en_test.yaml`, **Line No:** `4057`, **Line Pos:** `21` - **Line No:** `4057`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedResponseTypes > items`

94. **File:** `en_test.yaml`, **Line No:** `4076`, **Line Pos:** `21` - **Line No:** `4076`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAuthorizationDetailsTypes > items`

95. **File:** `en_test.yaml`, **Line No:** `4085`, **Line Pos:** `21` - **Line No:** `4085`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedServiceProfiles > items`

96. **File:** `en_test.yaml`, **Line No:** `4128`, **Line Pos:** `21` - **Line No:** `4128`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedUiLocales > items`

97. **File:** `en_test.yaml`, **Line No:** `4346`, **Line Pos:** `21` - **Line No:** `4346`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > trustedRootCertificates > items`

98. **File:** `en_test.yaml`, **Line No:** `4352`, **Line Pos:** `21` - **Line No:** `4352`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items`

99. **File:** `en_test.yaml`, **Line No:** `4355`, **Line Pos:** `25` - **Line No:** `4355`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > name`

100. **File:** `en_test.yaml`, **Line No:** `4357`, **Line Pos:** `25` - **Line No:** `4357`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > uri`

101. **File:** `en_test.yaml`, **Line No:** `4472`, **Line Pos:** `21` - **Line No:** `4472`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items`

102. **File:** `en_test.yaml`, **Line No:** `4487`, **Line Pos:** `27` - **Line No:** `4487`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

103. **File:** `en_test.yaml`, **Line No:** `4499`, **Line Pos:** `27` - **Line No:** `4499`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

104. **File:** `en_test.yaml`, **Line No:** `4555`, **Line Pos:** `21` - **Line No:** `4555`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimTypes > items`

105. **File:** `en_test.yaml`, **Line No:** `4569`, **Line Pos:** `21` - **Line No:** `4569`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimLocales > items`

106. **File:** `en_test.yaml`, **Line No:** `4580`, **Line Pos:** `21` - **Line No:** `4580`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaims > items`

107. **File:** `en_test.yaml`, **Line No:** `4767`, **Line Pos:** `21` - **Line No:** `4767`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

108. **File:** `en_test.yaml`, **Line No:** `4872`, **Line Pos:** `21` - **Line No:** `4872`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedTrustFrameworks > items`

109. **File:** `en_test.yaml`, **Line No:** `4879`, **Line Pos:** `21` - **Line No:** `4879`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedEvidence > items`

110. **File:** `en_test.yaml`, **Line No:** `4885`, **Line Pos:** `21` - **Line No:** `4885`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedIdentityDocuments > items`

111. **File:** `en_test.yaml`, **Line No:** `4892`, **Line Pos:** `21` - **Line No:** `4892`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedVerificationMethods > items`

112. **File:** `en_test.yaml`, **Line No:** `4899`, **Line Pos:** `21` - **Line No:** `4899`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedVerifiedClaims > items`

113. **File:** `en_test.yaml`, **Line No:** `4913`, **Line Pos:** `21` - **Line No:** `4913`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > attributes > items`

114. **File:** `en_test.yaml`, **Line No:** `4966`, **Line Pos:** `21` - **Line No:** `4966`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedCustomClientMetadata > items`

115. **File:** `en_test.yaml`, **Line No:** `5265`, **Line Pos:** `21` - **Line No:** `5265`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authorityHints > items`

116. **File:** `en_test.yaml`, **Line No:** `5339`, **Line Pos:** `21` - **Line No:** `5339`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDigestAlgorithms > items`

117. **File:** `en_test.yaml`, **Line No:** `5349`, **Line Pos:** `21` - **Line No:** `5349`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDocuments > items`

118. **File:** `en_test.yaml`, **Line No:** `5356`, **Line Pos:** `21` - **Line No:** `5356`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDocumentsMethods > items`

119. **File:** `en_test.yaml`, **Line No:** `5369`, **Line Pos:** `21` - **Line No:** `5369`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDocumentsValidationMethods > items`

120. **File:** `en_test.yaml`, **Line No:** `5378`, **Line Pos:** `21` - **Line No:** `5378`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDocumentsVerificationMethods > items`

121. **File:** `en_test.yaml`, **Line No:** `5387`, **Line Pos:** `21` - **Line No:** `5387`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedElectronicRecords > items`

122. **File:** `en_test.yaml`, **Line No:** `5394`, **Line Pos:** `19` - **Line No:** `5394`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClientRegistrationTypes`

123. **File:** `en_test.yaml`, **Line No:** `5454`, **Line Pos:** `21` - **Line No:** `5454`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > trustAnchors > items`

124. **File:** `en_test.yaml`, **Line No:** `5480`, **Line Pos:** `21` - **Line No:** `5480`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDocumentsCheckMethods > items`

125. **File:** `en_test.yaml`, **Line No:** `5573`, **Line Pos:** `21` - **Line No:** `5573`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > fapiModes > items`

126. **File:** `en_test.yaml`, **Line No:** `5597`, **Line Pos:** `19` - **Line No:** `5597`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata`

127. **File:** `en_test.yaml`, **Line No:** `5602`, **Line Pos:** `25` - **Line No:** `5602`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata > properties > authorizationServers > items`

128. **File:** `en_test.yaml`, **Line No:** `5626`, **Line Pos:** `25` - **Line No:** `5626`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

129. **File:** `en_test.yaml`, **Line No:** `5633`, **Line Pos:** `25` - **Line No:** `5633`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

130. **File:** `en_test.yaml`, **Line No:** `5700`, **Line Pos:** `15` - **Line No:** `5700`, **Line Pos:** `16`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema`

131. **File:** `en_test.yaml`, **Line No:** `5733`, **Line Pos:** `21` - **Line No:** `5733`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > metadata > items`

132. **File:** `en_test.yaml`, **Line No:** `5787`, **Line Pos:** `21` - **Line No:** `5787`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedAcrs > items`

133. **File:** `en_test.yaml`, **Line No:** `5817`, **Line Pos:** `21` - **Line No:** `5817`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedResponseTypes > items`

134. **File:** `en_test.yaml`, **Line No:** `5836`, **Line Pos:** `21` - **Line No:** `5836`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedAuthorizationDetailsTypes > items`

135. **File:** `en_test.yaml`, **Line No:** `5845`, **Line Pos:** `21` - **Line No:** `5845`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedServiceProfiles > items`

136. **File:** `en_test.yaml`, **Line No:** `5888`, **Line Pos:** `21` - **Line No:** `5888`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedUiLocales > items`

137. **File:** `en_test.yaml`, **Line No:** `6106`, **Line Pos:** `21` - **Line No:** `6106`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > trustedRootCertificates > items`

138. **File:** `en_test.yaml`, **Line No:** `6112`, **Line Pos:** `21` - **Line No:** `6112`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > mtlsEndpointAliases > items`

139. **File:** `en_test.yaml`, **Line No:** `6115`, **Line Pos:** `25` - **Line No:** `6115`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > mtlsEndpointAliases > items > properties > name`

140. **File:** `en_test.yaml`, **Line No:** `6117`, **Line Pos:** `25` - **Line No:** `6117`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > mtlsEndpointAliases > items > properties > uri`

141. **File:** `en_test.yaml`, **Line No:** `6232`, **Line Pos:** `21` - **Line No:** `6232`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items`

142. **File:** `en_test.yaml`, **Line No:** `6247`, **Line Pos:** `27` - **Line No:** `6247`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > descriptions > items`

143. **File:** `en_test.yaml`, **Line No:** `6259`, **Line Pos:** `27` - **Line No:** `6259`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedScopes > items > properties > attributes > items`

144. **File:** `en_test.yaml`, **Line No:** `6315`, **Line Pos:** `21` - **Line No:** `6315`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClaimTypes > items`

145. **File:** `en_test.yaml`, **Line No:** `6329`, **Line Pos:** `21` - **Line No:** `6329`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClaimLocales > items`

146. **File:** `en_test.yaml`, **Line No:** `6340`, **Line Pos:** `21` - **Line No:** `6340`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClaims > items`

147. **File:** `en_test.yaml`, **Line No:** `6527`, **Line Pos:** `21` - **Line No:** `6527`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedBackchannelTokenDeliveryModes > items`

148. **File:** `en_test.yaml`, **Line No:** `6632`, **Line Pos:** `21` - **Line No:** `6632`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedTrustFrameworks > items`

149. **File:** `en_test.yaml`, **Line No:** `6639`, **Line Pos:** `21` - **Line No:** `6639`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedEvidence > items`

150. **File:** `en_test.yaml`, **Line No:** `6645`, **Line Pos:** `21` - **Line No:** `6645`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedIdentityDocuments > items`

151. **File:** `en_test.yaml`, **Line No:** `6652`, **Line Pos:** `21` - **Line No:** `6652`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedVerificationMethods > items`

152. **File:** `en_test.yaml`, **Line No:** `6659`, **Line Pos:** `21` - **Line No:** `6659`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedVerifiedClaims > items`

153. **File:** `en_test.yaml`, **Line No:** `6673`, **Line Pos:** `21` - **Line No:** `6673`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > attributes > items`

154. **File:** `en_test.yaml`, **Line No:** `6726`, **Line Pos:** `21` - **Line No:** `6726`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedCustomClientMetadata > items`

155. **File:** `en_test.yaml`, **Line No:** `7025`, **Line Pos:** `21` - **Line No:** `7025`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > authorityHints > items`

156. **File:** `en_test.yaml`, **Line No:** `7099`, **Line Pos:** `21` - **Line No:** `7099`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDigestAlgorithms > items`

157. **File:** `en_test.yaml`, **Line No:** `7109`, **Line Pos:** `21` - **Line No:** `7109`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDocuments > items`

158. **File:** `en_test.yaml`, **Line No:** `7116`, **Line Pos:** `21` - **Line No:** `7116`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDocumentsMethods > items`

159. **File:** `en_test.yaml`, **Line No:** `7129`, **Line Pos:** `21` - **Line No:** `7129`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDocumentsValidationMethods > items`

160. **File:** `en_test.yaml`, **Line No:** `7138`, **Line Pos:** `21` - **Line No:** `7138`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDocumentsVerificationMethods > items`

161. **File:** `en_test.yaml`, **Line No:** `7147`, **Line Pos:** `21` - **Line No:** `7147`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedElectronicRecords > items`

162. **File:** `en_test.yaml`, **Line No:** `7154`, **Line Pos:** `19` - **Line No:** `7154`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedClientRegistrationTypes`

163. **File:** `en_test.yaml`, **Line No:** `7214`, **Line Pos:** `21` - **Line No:** `7214`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > trustAnchors > items`

164. **File:** `en_test.yaml`, **Line No:** `7240`, **Line Pos:** `21` - **Line No:** `7240`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > supportedDocumentsCheckMethods > items`

165. **File:** `en_test.yaml`, **Line No:** `7333`, **Line Pos:** `21` - **Line No:** `7333`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > fapiModes > items`

166. **File:** `en_test.yaml`, **Line No:** `7357`, **Line Pos:** `19` - **Line No:** `7357`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata`

167. **File:** `en_test.yaml`, **Line No:** `7362`, **Line Pos:** `25` - **Line No:** `7362`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata > properties > authorizationServers > items`

168. **File:** `en_test.yaml`, **Line No:** `7386`, **Line Pos:** `25` - **Line No:** `7386`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

169. **File:** `en_test.yaml`, **Line No:** `7393`, **Line Pos:** `25` - **Line No:** `7393`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/x-www-form-urlencoded > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

170. **File:** `en_test.yaml`, **Line No:** `7429`, **Line Pos:** `17` - **Line No:** `7429`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema`

171. **File:** `en_test.yaml`, **Line No:** `7462`, **Line Pos:** `23` - **Line No:** `7462`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > metadata > items`

172. **File:** `en_test.yaml`, **Line No:** `7516`, **Line Pos:** `23` - **Line No:** `7516`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedAcrs > items`

173. **File:** `en_test.yaml`, **Line No:** `7546`, **Line Pos:** `23` - **Line No:** `7546`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

174. **File:** `en_test.yaml`, **Line No:** `7565`, **Line Pos:** `23` - **Line No:** `7565`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedAuthorizationDetailsTypes > items`

175. **File:** `en_test.yaml`, **Line No:** `7574`, **Line Pos:** `23` - **Line No:** `7574`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

176. **File:** `en_test.yaml`, **Line No:** `7617`, **Line Pos:** `23` - **Line No:** `7617`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedUiLocales > items`

177. **File:** `en_test.yaml`, **Line No:** `7835`, **Line Pos:** `23` - **Line No:** `7835`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > trustedRootCertificates > items`

178. **File:** `en_test.yaml`, **Line No:** `7841`, **Line Pos:** `23` - **Line No:** `7841`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

179. **File:** `en_test.yaml`, **Line No:** `7844`, **Line Pos:** `27` - **Line No:** `7844`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > name`

180. **File:** `en_test.yaml`, **Line No:** `7846`, **Line Pos:** `27` - **Line No:** `7846`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > uri`

181. **File:** `en_test.yaml`, **Line No:** `7961`, **Line Pos:** `23` - **Line No:** `7961`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

182. **File:** `en_test.yaml`, **Line No:** `7976`, **Line Pos:** `29` - **Line No:** `7976`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

183. **File:** `en_test.yaml`, **Line No:** `7988`, **Line Pos:** `29` - **Line No:** `7988`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

184. **File:** `en_test.yaml`, **Line No:** `8044`, **Line Pos:** `23` - **Line No:** `8044`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

185. **File:** `en_test.yaml`, **Line No:** `8058`, **Line Pos:** `23` - **Line No:** `8058`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClaimLocales > items`

186. **File:** `en_test.yaml`, **Line No:** `8069`, **Line Pos:** `23` - **Line No:** `8069`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClaims > items`

187. **File:** `en_test.yaml`, **Line No:** `8256`, **Line Pos:** `23` - **Line No:** `8256`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

188. **File:** `en_test.yaml`, **Line No:** `8361`, **Line Pos:** `23` - **Line No:** `8361`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedTrustFrameworks > items`

189. **File:** `en_test.yaml`, **Line No:** `8368`, **Line Pos:** `23` - **Line No:** `8368`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedEvidence > items`

190. **File:** `en_test.yaml`, **Line No:** `8374`, **Line Pos:** `23` - **Line No:** `8374`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedIdentityDocuments > items`

191. **File:** `en_test.yaml`, **Line No:** `8381`, **Line Pos:** `23` - **Line No:** `8381`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedVerificationMethods > items`

192. **File:** `en_test.yaml`, **Line No:** `8388`, **Line Pos:** `23` - **Line No:** `8388`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedVerifiedClaims > items`

193. **File:** `en_test.yaml`, **Line No:** `8402`, **Line Pos:** `23` - **Line No:** `8402`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > attributes > items`

194. **File:** `en_test.yaml`, **Line No:** `8455`, **Line Pos:** `23` - **Line No:** `8455`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedCustomClientMetadata > items`

195. **File:** `en_test.yaml`, **Line No:** `8754`, **Line Pos:** `23` - **Line No:** `8754`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > authorityHints > items`

196. **File:** `en_test.yaml`, **Line No:** `8828`, **Line Pos:** `23` - **Line No:** `8828`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDigestAlgorithms > items`

197. **File:** `en_test.yaml`, **Line No:** `8838`, **Line Pos:** `23` - **Line No:** `8838`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDocuments > items`

198. **File:** `en_test.yaml`, **Line No:** `8845`, **Line Pos:** `23` - **Line No:** `8845`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDocumentsMethods > items`

199. **File:** `en_test.yaml`, **Line No:** `8858`, **Line Pos:** `23` - **Line No:** `8858`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDocumentsValidationMethods > items`

200. **File:** `en_test.yaml`, **Line No:** `8867`, **Line Pos:** `23` - **Line No:** `8867`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDocumentsVerificationMethods > items`

201. **File:** `en_test.yaml`, **Line No:** `8876`, **Line Pos:** `23` - **Line No:** `8876`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedElectronicRecords > items`

202. **File:** `en_test.yaml`, **Line No:** `8883`, **Line Pos:** `21` - **Line No:** `8883`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes`

203. **File:** `en_test.yaml`, **Line No:** `8943`, **Line Pos:** `23` - **Line No:** `8943`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

204. **File:** `en_test.yaml`, **Line No:** `8969`, **Line Pos:** `23` - **Line No:** `8969`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > supportedDocumentsCheckMethods > items`

205. **File:** `en_test.yaml`, **Line No:** `9062`, **Line Pos:** `23` - **Line No:** `9062`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > fapiModes > items`

206. **File:** `en_test.yaml`, **Line No:** `9086`, **Line Pos:** `21` - **Line No:** `9086`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

207. **File:** `en_test.yaml`, **Line No:** `9091`, **Line Pos:** `27` - **Line No:** `9091`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > authorizationServers > items`

208. **File:** `en_test.yaml`, **Line No:** `9115`, **Line Pos:** `27` - **Line No:** `9115`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

209. **File:** `en_test.yaml`, **Line No:** `9122`, **Line Pos:** `27` - **Line No:** `9122`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

210. **File:** `en_test.yaml`, **Line No:** `9249`, **Line Pos:** `17` - **Line No:** `9249`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 400 > content > application/json > schema`

211. **File:** `en_test.yaml`, **Line No:** `9265`, **Line Pos:** `17` - **Line No:** `9265`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 401 > content > application/json > schema`

212. **File:** `en_test.yaml`, **Line No:** `9281`, **Line Pos:** `17` - **Line No:** `9281`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 403 > content > application/json > schema`

213. **File:** `en_test.yaml`, **Line No:** `9297`, **Line Pos:** `17` - **Line No:** `9297`, **Line Pos:** `18`, **Path:** `# > paths > /api/service/create > post > responses > 500 > content > application/json > schema`

214. **File:** `en_test.yaml`, **Line No:** `9343`, **Line Pos:** `7` - **Line No:** `9343`, **Line Pos:** `8`, **Path:** `# > components > schemas > AccessToken`

215. **File:** `en_test.yaml`, **Line No:** `9395`, **Line Pos:** `13` - **Line No:** `9395`, **Line Pos:** `14`, **Path:** `# > components > schemas > AccessToken > properties > scopes > items`

216. **File:** `en_test.yaml`, **Line No:** `9401`, **Line Pos:** `13` - **Line No:** `9401`, **Line Pos:** `14`, **Path:** `# > components > schemas > AccessToken > properties > properties > items`

217. **File:** `en_test.yaml`, **Line No:** `9419`, **Line Pos:** `13` - **Line No:** `9419`, **Line Pos:** `14`, **Path:** `# > components > schemas > AccessToken > properties > refreshTokenScopes > items`

218. **File:** `en_test.yaml`, **Line No:** `9440`, **Line Pos:** `13` - **Line No:** `9440`, **Line Pos:** `14`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items`

219. **File:** `en_test.yaml`, **Line No:** `9456`, **Line Pos:** `19` - **Line No:** `9456`, **Line Pos:** `20`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items > properties > locations > items`

220. **File:** `en_test.yaml`, **Line No:** `9467`, **Line Pos:** `19` - **Line No:** `9467`, **Line Pos:** `20`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items > properties > actions > items`

221. **File:** `en_test.yaml`, **Line No:** `9478`, **Line Pos:** `19` - **Line No:** `9478`, **Line Pos:** `20`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items > properties > dataTypes > items`

222. **File:** `en_test.yaml`, **Line No:** `9494`, **Line Pos:** `19` - **Line No:** `9494`, **Line Pos:** `20`, **Path:** `# > components > schemas > AuthorizationDetails > properties > elements > items > properties > privileges > items`


### <a id="info-issue-no-14---schema-object-exampledefault-value-is-missing-604"></a> `Info` Issue No. 14 - Schema object example/default value is missing. (604)

| Property | Value |
| -------- | ----- |
| Rule Id | `schema-example-or-default-value-exists` |
| Ruleset Id | `openapi-v3-docsgen-linting` |
| Type of Issue | Semantic |
| Broad Category of Issue | OpenAPI Schemas |
| Possible Impact On Output Of | `Developer Experience Portal` |

Schema Object must specify a non-null, non-empty example value using the `example` property or a default value using the `default` property if applicable.

#### <a id="tips-14"></a> Tips

* If the schema definition has a default value, it must be specified using the `default` value.
* If the schema has no default value, ensure that the `example` property is present in the Schema Object.
* Ensure that the schema example or default value is not empty or null.
* The example or default value specified must be valid in accordance with the schema type definition.

#### <a id="for-more-information-14"></a> For More Information

* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schema-object
* https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md

#### <a id="affected-components-604"></a> Affected Components (`604`)

1. **File:** `en_test.yaml`, **Line No:** `26`, **Line Pos:** `13` - **Line No:** `26`, **Line Pos:** `14`, **Path:** `# > paths > /api/{serviceId}/service/get > get > parameters > 0 > schema`

2. **File:** `en_test.yaml`, **Line No:** `37`, **Line Pos:** `21` - **Line No:** `37`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > number`

3. **File:** `en_test.yaml`, **Line No:** `42`, **Line Pos:** `21` - **Line No:** `42`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > serviceName`

4. **File:** `en_test.yaml`, **Line No:** `45`, **Line Pos:** `21` - **Line No:** `45`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > issuer`

5. **File:** `en_test.yaml`, **Line No:** `54`, **Line Pos:** `21` - **Line No:** `54`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > description`

6. **File:** `en_test.yaml`, **Line No:** `57`, **Line Pos:** `21` - **Line No:** `57`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > apiKey`

7. **File:** `en_test.yaml`, **Line No:** `62`, **Line Pos:** `21` - **Line No:** `62`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > clientIdAliasEnabled`

8. **File:** `en_test.yaml`, **Line No:** `65`, **Line Pos:** `21` - **Line No:** `65`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata`

9. **File:** `en_test.yaml`, **Line No:** `67`, **Line Pos:** `23` - **Line No:** `67`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata > items`

10. **File:** `en_test.yaml`, **Line No:** `70`, **Line Pos:** `27` - **Line No:** `70`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata > items > properties > key`

11. **File:** `en_test.yaml`, **Line No:** `73`, **Line Pos:** `27` - **Line No:** `73`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > metadata > items > properties > value`

12. **File:** `en_test.yaml`, **Line No:** `83`, **Line Pos:** `21` - **Line No:** `83`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > createdAt`

13. **File:** `en_test.yaml`, **Line No:** `90`, **Line Pos:** `21` - **Line No:** `90`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > modifiedAt`

14. **File:** `en_test.yaml`, **Line No:** `97`, **Line Pos:** `21` - **Line No:** `97`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authenticationCallbackEndpoint`

15. **File:** `en_test.yaml`, **Line No:** `108`, **Line Pos:** `21` - **Line No:** `108`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authenticationCallbackApiKey`

16. **File:** `en_test.yaml`, **Line No:** `115`, **Line Pos:** `21` - **Line No:** `115`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authenticationCallbackApiSecret`

17. **File:** `en_test.yaml`, **Line No:** `118`, **Line Pos:** `21` - **Line No:** `118`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAcrs`

18. **File:** `en_test.yaml`, **Line No:** `121`, **Line Pos:** `23` - **Line No:** `121`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAcrs > items`

19. **File:** `en_test.yaml`, **Line No:** `128`, **Line Pos:** `21` - **Line No:** `128`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedGrantTypes`

20. **File:** `en_test.yaml`, **Line No:** `130`, **Line Pos:** `23` - **Line No:** `130`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedGrantTypes > items`

21. **File:** `en_test.yaml`, **Line No:** `149`, **Line Pos:** `21` - **Line No:** `149`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedResponseTypes`

22. **File:** `en_test.yaml`, **Line No:** `151`, **Line Pos:** `23` - **Line No:** `151`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedResponseTypes > items`

23. **File:** `en_test.yaml`, **Line No:** `168`, **Line Pos:** `21` - **Line No:** `168`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAuthorizationDetailsTypes`

24. **File:** `en_test.yaml`, **Line No:** `170`, **Line Pos:** `23` - **Line No:** `170`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAuthorizationDetailsTypes > items`

25. **File:** `en_test.yaml`, **Line No:** `177`, **Line Pos:** `21` - **Line No:** `177`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles`

26. **File:** `en_test.yaml`, **Line No:** `179`, **Line Pos:** `23` - **Line No:** `179`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedServiceProfiles > items`

27. **File:** `en_test.yaml`, **Line No:** `186`, **Line Pos:** `21` - **Line No:** `186`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > errorDescriptionOmitted`

28. **File:** `en_test.yaml`, **Line No:** `195`, **Line Pos:** `21` - **Line No:** `195`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > errorUriOmitted`

29. **File:** `en_test.yaml`, **Line No:** `204`, **Line Pos:** `21` - **Line No:** `204`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authorizationEndpoint`

30. **File:** `en_test.yaml`, **Line No:** `214`, **Line Pos:** `21` - **Line No:** `214`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directAuthorizationEndpointEnabled`

31. **File:** `en_test.yaml`, **Line No:** `220`, **Line Pos:** `21` - **Line No:** `220`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedUiLocales`

32. **File:** `en_test.yaml`, **Line No:** `222`, **Line Pos:** `23` - **Line No:** `222`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedUiLocales > items`

33. **File:** `en_test.yaml`, **Line No:** `230`, **Line Pos:** `21` - **Line No:** `230`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDisplays`

34. **File:** `en_test.yaml`, **Line No:** `232`, **Line Pos:** `23` - **Line No:** `232`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDisplays > items`

35. **File:** `en_test.yaml`, **Line No:** `253`, **Line Pos:** `21` - **Line No:** `253`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > pkceRequired`

36. **File:** `en_test.yaml`, **Line No:** `261`, **Line Pos:** `21` - **Line No:** `261`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > pkceS256Required`

37. **File:** `en_test.yaml`, **Line No:** `269`, **Line Pos:** `21` - **Line No:** `269`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authorizationResponseDuration`

38. **File:** `en_test.yaml`, **Line No:** `280`, **Line Pos:** `21` - **Line No:** `280`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenEndpoint`

39. **File:** `en_test.yaml`, **Line No:** `290`, **Line Pos:** `21` - **Line No:** `290`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directTokenEndpointEnabled`

40. **File:** `en_test.yaml`, **Line No:** `295`, **Line Pos:** `21` - **Line No:** `295`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods`

41. **File:** `en_test.yaml`, **Line No:** `297`, **Line Pos:** `23` - **Line No:** `297`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTokenAuthMethods > items`

42. **File:** `en_test.yaml`, **Line No:** `316`, **Line Pos:** `21` - **Line No:** `316`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > missingClientIdAllowed`

43. **File:** `en_test.yaml`, **Line No:** `322`, **Line Pos:** `21` - **Line No:** `322`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > revocationEndpoint`

44. **File:** `en_test.yaml`, **Line No:** `329`, **Line Pos:** `21` - **Line No:** `329`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directRevocationEndpointEnabled`

45. **File:** `en_test.yaml`, **Line No:** `332`, **Line Pos:** `21` - **Line No:** `332`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods`

46. **File:** `en_test.yaml`, **Line No:** `334`, **Line Pos:** `23` - **Line No:** `334`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

47. **File:** `en_test.yaml`, **Line No:** `350`, **Line Pos:** `21` - **Line No:** `350`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > introspectionEndpoint`

48. **File:** `en_test.yaml`, **Line No:** `354`, **Line Pos:** `21` - **Line No:** `354`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directIntrospectionEndpointEnabled`

49. **File:** `en_test.yaml`, **Line No:** `357`, **Line Pos:** `21` - **Line No:** `357`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods`

50. **File:** `en_test.yaml`, **Line No:** `361`, **Line Pos:** `23` - **Line No:** `361`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

51. **File:** `en_test.yaml`, **Line No:** `375`, **Line Pos:** `21` - **Line No:** `375`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > pushedAuthReqEndpoint`

52. **File:** `en_test.yaml`, **Line No:** `382`, **Line Pos:** `21` - **Line No:** `382`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > pushedAuthReqDuration`

53. **File:** `en_test.yaml`, **Line No:** `396`, **Line Pos:** `21` - **Line No:** `396`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > parRequired`

54. **File:** `en_test.yaml`, **Line No:** `404`, **Line Pos:** `21` - **Line No:** `404`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > requestObjectRequired`

55. **File:** `en_test.yaml`, **Line No:** `415`, **Line Pos:** `21` - **Line No:** `415`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > traditionalRequestObjectProcessingApplied`

56. **File:** `en_test.yaml`, **Line No:** `434`, **Line Pos:** `21` - **Line No:** `434`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mutualTlsValidatePkiCertChain`

57. **File:** `en_test.yaml`, **Line No:** `438`, **Line Pos:** `21` - **Line No:** `438`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustedRootCertificates`

58. **File:** `en_test.yaml`, **Line No:** `440`, **Line Pos:** `23` - **Line No:** `440`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustedRootCertificates > items`

59. **File:** `en_test.yaml`, **Line No:** `444`, **Line Pos:** `21` - **Line No:** `444`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases`

60. **File:** `en_test.yaml`, **Line No:** `446`, **Line Pos:** `23` - **Line No:** `446`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items`

61. **File:** `en_test.yaml`, **Line No:** `449`, **Line Pos:** `27` - **Line No:** `449`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > name`

62. **File:** `en_test.yaml`, **Line No:** `451`, **Line Pos:** `27` - **Line No:** `451`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > uri`

63. **File:** `en_test.yaml`, **Line No:** `471`, **Line Pos:** `21` - **Line No:** `471`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenType`

64. **File:** `en_test.yaml`, **Line No:** `481`, **Line Pos:** `21` - **Line No:** `481`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tlsClientCertificateBoundAccessTokens`

65. **File:** `en_test.yaml`, **Line No:** `485`, **Line Pos:** `21` - **Line No:** `485`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenDuration`

66. **File:** `en_test.yaml`, **Line No:** `491`, **Line Pos:** `21` - **Line No:** `491`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > singleAccessTokenPerSubject`

67. **File:** `en_test.yaml`, **Line No:** `499`, **Line Pos:** `21` - **Line No:** `499`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenSignAlg`

68. **File:** `en_test.yaml`, **Line No:** `525`, **Line Pos:** `21` - **Line No:** `525`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenSignatureKeyId`

69. **File:** `en_test.yaml`, **Line No:** `536`, **Line Pos:** `21` - **Line No:** `536`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > refreshTokenDuration`

70. **File:** `en_test.yaml`, **Line No:** `540`, **Line Pos:** `21` - **Line No:** `540`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > refreshTokenDurationKept`

71. **File:** `en_test.yaml`, **Line No:** `545`, **Line Pos:** `21` - **Line No:** `545`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > refreshTokenDurationReset`

72. **File:** `en_test.yaml`, **Line No:** `556`, **Line Pos:** `21` - **Line No:** `556`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > refreshTokenKept`

73. **File:** `en_test.yaml`, **Line No:** `564`, **Line Pos:** `21` - **Line No:** `564`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes`

74. **File:** `en_test.yaml`, **Line No:** `566`, **Line Pos:** `23` - **Line No:** `566`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items`

75. **File:** `en_test.yaml`, **Line No:** `569`, **Line Pos:** `27` - **Line No:** `569`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > name`

76. **File:** `en_test.yaml`, **Line No:** `572`, **Line Pos:** `27` - **Line No:** `572`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > defaultEntry`

77. **File:** `en_test.yaml`, **Line No:** `575`, **Line Pos:** `27` - **Line No:** `575`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > description`

78. **File:** `en_test.yaml`, **Line No:** `578`, **Line Pos:** `27` - **Line No:** `578`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions`

79. **File:** `en_test.yaml`, **Line No:** `581`, **Line Pos:** `29` - **Line No:** `581`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

80. **File:** `en_test.yaml`, **Line No:** `584`, **Line Pos:** `33` - **Line No:** `584`, **Line Pos:** `34`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items > properties > tag`

81. **File:** `en_test.yaml`, **Line No:** `587`, **Line Pos:** `33` - **Line No:** `587`, **Line Pos:** `34`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items > properties > value`

82. **File:** `en_test.yaml`, **Line No:** `590`, **Line Pos:** `27` - **Line No:** `590`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes`

83. **File:** `en_test.yaml`, **Line No:** `593`, **Line Pos:** `29` - **Line No:** `593`, **Line Pos:** `30`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

84. **File:** `en_test.yaml`, **Line No:** `596`, **Line Pos:** `33` - **Line No:** `596`, **Line Pos:** `34`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items > properties > key`

85. **File:** `en_test.yaml`, **Line No:** `599`, **Line Pos:** `33` - **Line No:** `599`, **Line Pos:** `34`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items > properties > value`

86. **File:** `en_test.yaml`, **Line No:** `617`, **Line Pos:** `21` - **Line No:** `617`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > scopeRequired`

87. **File:** `en_test.yaml`, **Line No:** `634`, **Line Pos:** `21` - **Line No:** `634`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > idTokenDuration`

88. **File:** `en_test.yaml`, **Line No:** `640`, **Line Pos:** `21` - **Line No:** `640`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > allowableClockSkew`

89. **File:** `en_test.yaml`, **Line No:** `647`, **Line Pos:** `21` - **Line No:** `647`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimTypes`

90. **File:** `en_test.yaml`, **Line No:** `649`, **Line Pos:** `23` - **Line No:** `649`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimTypes > items`

91. **File:** `en_test.yaml`, **Line No:** `661`, **Line Pos:** `21` - **Line No:** `661`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimLocales`

92. **File:** `en_test.yaml`, **Line No:** `663`, **Line Pos:** `23` - **Line No:** `663`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaimLocales > items`

93. **File:** `en_test.yaml`, **Line No:** `672`, **Line Pos:** `21` - **Line No:** `672`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaims`

94. **File:** `en_test.yaml`, **Line No:** `674`, **Line Pos:** `23` - **Line No:** `674`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClaims > items`

95. **File:** `en_test.yaml`, **Line No:** `707`, **Line Pos:** `21` - **Line No:** `707`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > claimShortcutRestrictive`

96. **File:** `en_test.yaml`, **Line No:** `720`, **Line Pos:** `21` - **Line No:** `720`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > jwksUri`

97. **File:** `en_test.yaml`, **Line No:** `733`, **Line Pos:** `21` - **Line No:** `733`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directJwksEndpointEnabled`

98. **File:** `en_test.yaml`, **Line No:** `738`, **Line Pos:** `21` - **Line No:** `738`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > jwks`

99. **File:** `en_test.yaml`, **Line No:** `748`, **Line Pos:** `21` - **Line No:** `748`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > idTokenSignatureKeyId`

100. **File:** `en_test.yaml`, **Line No:** `765`, **Line Pos:** `21` - **Line No:** `765`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userInfoSignatureKeyId`

101. **File:** `en_test.yaml`, **Line No:** `782`, **Line Pos:** `21` - **Line No:** `782`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authorizationSignatureKeyId`

102. **File:** `en_test.yaml`, **Line No:** `798`, **Line Pos:** `21` - **Line No:** `798`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userInfoEndpoint`

103. **File:** `en_test.yaml`, **Line No:** `806`, **Line Pos:** `21` - **Line No:** `806`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > directUserInfoEndpointEnabled`

104. **File:** `en_test.yaml`, **Line No:** `811`, **Line Pos:** `21` - **Line No:** `811`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > dynamicRegistrationSupported`

105. **File:** `en_test.yaml`, **Line No:** `816`, **Line Pos:** `21` - **Line No:** `816`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > registrationEndpoint`

106. **File:** `en_test.yaml`, **Line No:** `824`, **Line Pos:** `21` - **Line No:** `824`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > registrationManagementEndpoint`

107. **File:** `en_test.yaml`, **Line No:** `832`, **Line Pos:** `21` - **Line No:** `832`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > policyUri`

108. **File:** `en_test.yaml`, **Line No:** `839`, **Line Pos:** `21` - **Line No:** `839`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tosUri`

109. **File:** `en_test.yaml`, **Line No:** `846`, **Line Pos:** `21` - **Line No:** `846`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > serviceDocumentation`

110. **File:** `en_test.yaml`, **Line No:** `853`, **Line Pos:** `21` - **Line No:** `853`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > backchannelAuthenticationEndpoint`

111. **File:** `en_test.yaml`, **Line No:** `859`, **Line Pos:** `21` - **Line No:** `859`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes`

112. **File:** `en_test.yaml`, **Line No:** `861`, **Line Pos:** `23` - **Line No:** `861`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedBackchannelTokenDeliveryModes > items`

113. **File:** `en_test.yaml`, **Line No:** `873`, **Line Pos:** `21` - **Line No:** `873`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > backchannelAuthReqIdDuration`

114. **File:** `en_test.yaml`, **Line No:** `880`, **Line Pos:** `21` - **Line No:** `880`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > backchannelPollingInterval`

115. **File:** `en_test.yaml`, **Line No:** `887`, **Line Pos:** `21` - **Line No:** `887`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > backchannelUserCodeParameterSupported`

116. **File:** `en_test.yaml`, **Line No:** `893`, **Line Pos:** `21` - **Line No:** `893`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > backchannelBindingMessageRequiredInFapi`

117. **File:** `en_test.yaml`, **Line No:** `907`, **Line Pos:** `21` - **Line No:** `907`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > deviceAuthorizationEndpoint`

118. **File:** `en_test.yaml`, **Line No:** `914`, **Line Pos:** `21` - **Line No:** `914`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > deviceVerificationUri`

119. **File:** `en_test.yaml`, **Line No:** `920`, **Line Pos:** `21` - **Line No:** `920`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > deviceVerificationUriComplete`

120. **File:** `en_test.yaml`, **Line No:** `938`, **Line Pos:** `21` - **Line No:** `938`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > deviceFlowCodeDuration`

121. **File:** `en_test.yaml`, **Line No:** `945`, **Line Pos:** `21` - **Line No:** `945`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > deviceFlowPollingInterval`

122. **File:** `en_test.yaml`, **Line No:** `952`, **Line Pos:** `21` - **Line No:** `952`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userCodeCharset`

123. **File:** `en_test.yaml`, **Line No:** `959`, **Line Pos:** `21` - **Line No:** `959`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userCodeLength`

124. **File:** `en_test.yaml`, **Line No:** `964`, **Line Pos:** `21` - **Line No:** `964`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTrustFrameworks`

125. **File:** `en_test.yaml`, **Line No:** `966`, **Line Pos:** `23` - **Line No:** `966`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedTrustFrameworks > items`

126. **File:** `en_test.yaml`, **Line No:** `971`, **Line Pos:** `21` - **Line No:** `971`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedEvidence`

127. **File:** `en_test.yaml`, **Line No:** `973`, **Line Pos:** `23` - **Line No:** `973`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedEvidence > items`

128. **File:** `en_test.yaml`, **Line No:** `977`, **Line Pos:** `21` - **Line No:** `977`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIdentityDocuments`

129. **File:** `en_test.yaml`, **Line No:** `979`, **Line Pos:** `23` - **Line No:** `979`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedIdentityDocuments > items`

130. **File:** `en_test.yaml`, **Line No:** `984`, **Line Pos:** `21` - **Line No:** `984`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedVerificationMethods`

131. **File:** `en_test.yaml`, **Line No:** `986`, **Line Pos:** `23` - **Line No:** `986`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedVerificationMethods > items`

132. **File:** `en_test.yaml`, **Line No:** `991`, **Line Pos:** `21` - **Line No:** `991`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedVerifiedClaims`

133. **File:** `en_test.yaml`, **Line No:** `993`, **Line Pos:** `23` - **Line No:** `993`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedVerifiedClaims > items`

134. **File:** `en_test.yaml`, **Line No:** `998`, **Line Pos:** `21` - **Line No:** `998`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > verifiedClaimsValidationSchemaSet`

135. **File:** `en_test.yaml`, **Line No:** `1005`, **Line Pos:** `21` - **Line No:** `1005`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes`

136. **File:** `en_test.yaml`, **Line No:** `1007`, **Line Pos:** `23` - **Line No:** `1007`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes > items`

137. **File:** `en_test.yaml`, **Line No:** `1010`, **Line Pos:** `27` - **Line No:** `1010`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes > items > properties > key`

138. **File:** `en_test.yaml`, **Line No:** `1013`, **Line Pos:** `27` - **Line No:** `1013`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > attributes > items > properties > value`

139. **File:** `en_test.yaml`, **Line No:** `1018`, **Line Pos:** `21` - **Line No:** `1018`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > nbfOptional`

140. **File:** `en_test.yaml`, **Line No:** `1041`, **Line Pos:** `21` - **Line No:** `1041`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > issSuppressed`

141. **File:** `en_test.yaml`, **Line No:** `1058`, **Line Pos:** `21` - **Line No:** `1058`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedCustomClientMetadata`

142. **File:** `en_test.yaml`, **Line No:** `1060`, **Line Pos:** `23` - **Line No:** `1060`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedCustomClientMetadata > items`

143. **File:** `en_test.yaml`, **Line No:** `1084`, **Line Pos:** `21` - **Line No:** `1084`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenExpirationLinked`

144. **File:** `en_test.yaml`, **Line No:** `1106`, **Line Pos:** `21` - **Line No:** `1106`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > frontChannelRequestObjectEncryptionRequired`

145. **File:** `en_test.yaml`, **Line No:** `1122`, **Line Pos:** `21` - **Line No:** `1122`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > requestObjectEncryptionAlgMatchRequired`

146. **File:** `en_test.yaml`, **Line No:** `1150`, **Line Pos:** `21` - **Line No:** `1150`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > requestObjectEncryptionEncMatchRequired`

147. **File:** `en_test.yaml`, **Line No:** `1171`, **Line Pos:** `21` - **Line No:** `1171`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsmEnabled`

148. **File:** `en_test.yaml`, **Line No:** `1181`, **Line Pos:** `21` - **Line No:** `1181`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks`

149. **File:** `en_test.yaml`, **Line No:** `1183`, **Line Pos:** `23` - **Line No:** `1183`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items`

150. **File:** `en_test.yaml`, **Line No:** `1188`, **Line Pos:** `27` - **Line No:** `1188`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > kty`

151. **File:** `en_test.yaml`, **Line No:** `1192`, **Line Pos:** `27` - **Line No:** `1192`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > use`

152. **File:** `en_test.yaml`, **Line No:** `1198`, **Line Pos:** `27` - **Line No:** `1198`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > kid`

153. **File:** `en_test.yaml`, **Line No:** `1202`, **Line Pos:** `27` - **Line No:** `1202`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > hsmName`

154. **File:** `en_test.yaml`, **Line No:** `1207`, **Line Pos:** `27` - **Line No:** `1207`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > handle`

155. **File:** `en_test.yaml`, **Line No:** `1212`, **Line Pos:** `27` - **Line No:** `1212`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > publicKey`

156. **File:** `en_test.yaml`, **Line No:** `1216`, **Line Pos:** `27` - **Line No:** `1216`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > hsks > items > properties > alg`

157. **File:** `en_test.yaml`, **Line No:** `1228`, **Line Pos:** `21` - **Line No:** `1228`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > grantManagementEndpoint`

158. **File:** `en_test.yaml`, **Line No:** `1232`, **Line Pos:** `21` - **Line No:** `1232`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > grantManagementActionRequired`

159. **File:** `en_test.yaml`, **Line No:** `1245`, **Line Pos:** `21` - **Line No:** `1245`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > unauthorizedOnClientConfigSupported`

160. **File:** `en_test.yaml`, **Line No:** `1266`, **Line Pos:** `21` - **Line No:** `1266`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > dcrScopeUsedAsRequestable`

161. **File:** `en_test.yaml`, **Line No:** `1277`, **Line Pos:** `21` - **Line No:** `1277`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > endSessionEndpoint`

162. **File:** `en_test.yaml`, **Line No:** `1287`, **Line Pos:** `21` - **Line No:** `1287`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > loopbackRedirectionUriVariable`

163. **File:** `en_test.yaml`, **Line No:** `1329`, **Line Pos:** `21` - **Line No:** `1329`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > requestObjectAudienceChecked`

164. **File:** `en_test.yaml`, **Line No:** `1351`, **Line Pos:** `21` - **Line No:** `1351`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > accessTokenForExternalAttachmentEmbedded`

165. **File:** `en_test.yaml`, **Line No:** `1357`, **Line Pos:** `21` - **Line No:** `1357`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authorityHints`

166. **File:** `en_test.yaml`, **Line No:** `1359`, **Line Pos:** `23` - **Line No:** `1359`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > authorityHints > items`

167. **File:** `en_test.yaml`, **Line No:** `1366`, **Line Pos:** `21` - **Line No:** `1366`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > federationEnabled`

168. **File:** `en_test.yaml`, **Line No:** `1370`, **Line Pos:** `21` - **Line No:** `1370`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > federationJwks`

169. **File:** `en_test.yaml`, **Line No:** `1376`, **Line Pos:** `21` - **Line No:** `1376`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > federationSignatureKeyId`

170. **File:** `en_test.yaml`, **Line No:** `1381`, **Line Pos:** `21` - **Line No:** `1381`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > federationConfigurationDuration`

171. **File:** `en_test.yaml`, **Line No:** `1385`, **Line Pos:** `21` - **Line No:** `1385`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > federationRegistrationEndpoint`

172. **File:** `en_test.yaml`, **Line No:** `1391`, **Line Pos:** `21` - **Line No:** `1391`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > organizationName`

173. **File:** `en_test.yaml`, **Line No:** `1397`, **Line Pos:** `21` - **Line No:** `1397`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > predefinedTransformedClaims`

174. **File:** `en_test.yaml`, **Line No:** `1403`, **Line Pos:** `21` - **Line No:** `1403`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > refreshTokenIdempotent`

175. **File:** `en_test.yaml`, **Line No:** `1410`, **Line Pos:** `21` - **Line No:** `1410`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > signedJwksUri`

176. **File:** `en_test.yaml`, **Line No:** `1416`, **Line Pos:** `21` - **Line No:** `1416`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAttachments`

177. **File:** `en_test.yaml`, **Line No:** `1418`, **Line Pos:** `23` - **Line No:** `1418`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedAttachments > items`

178. **File:** `en_test.yaml`, **Line No:** `1431`, **Line Pos:** `21` - **Line No:** `1431`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDigestAlgorithms`

179. **File:** `en_test.yaml`, **Line No:** `1433`, **Line Pos:** `23` - **Line No:** `1433`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDigestAlgorithms > items`

180. **File:** `en_test.yaml`, **Line No:** `1441`, **Line Pos:** `21` - **Line No:** `1441`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocuments`

181. **File:** `en_test.yaml`, **Line No:** `1443`, **Line Pos:** `23` - **Line No:** `1443`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocuments > items`

182. **File:** `en_test.yaml`, **Line No:** `1448`, **Line Pos:** `21` - **Line No:** `1448`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsMethods`

183. **File:** `en_test.yaml`, **Line No:** `1450`, **Line Pos:** `23` - **Line No:** `1450`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsMethods > items`

184. **File:** `en_test.yaml`, **Line No:** `1461`, **Line Pos:** `21` - **Line No:** `1461`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsValidationMethods`

185. **File:** `en_test.yaml`, **Line No:** `1463`, **Line Pos:** `23` - **Line No:** `1463`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsValidationMethods > items`

186. **File:** `en_test.yaml`, **Line No:** `1470`, **Line Pos:** `21` - **Line No:** `1470`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsVerificationMethods`

187. **File:** `en_test.yaml`, **Line No:** `1472`, **Line Pos:** `23` - **Line No:** `1472`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsVerificationMethods > items`

188. **File:** `en_test.yaml`, **Line No:** `1479`, **Line Pos:** `21` - **Line No:** `1479`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedElectronicRecords`

189. **File:** `en_test.yaml`, **Line No:** `1481`, **Line Pos:** `23` - **Line No:** `1481`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedElectronicRecords > items`

190. **File:** `en_test.yaml`, **Line No:** `1488`, **Line Pos:** `21` - **Line No:** `1488`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes`

191. **File:** `en_test.yaml`, **Line No:** `1490`, **Line Pos:** `23` - **Line No:** `1490`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedClientRegistrationTypes > items`

192. **File:** `en_test.yaml`, **Line No:** `1499`, **Line Pos:** `21` - **Line No:** `1499`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenExchangeByIdentifiableClientsOnly`

193. **File:** `en_test.yaml`, **Line No:** `1504`, **Line Pos:** `21` - **Line No:** `1504`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenExchangeByConfidentialClientsOnly`

194. **File:** `en_test.yaml`, **Line No:** `1509`, **Line Pos:** `21` - **Line No:** `1509`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenExchangeByPermittedClientsOnly`

195. **File:** `en_test.yaml`, **Line No:** `1514`, **Line Pos:** `21` - **Line No:** `1514`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenExchangeEncryptedJwtRejected`

196. **File:** `en_test.yaml`, **Line No:** `1519`, **Line Pos:** `21` - **Line No:** `1519`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > tokenExchangeUnsignedJwtRejected`

197. **File:** `en_test.yaml`, **Line No:** `1524`, **Line Pos:** `21` - **Line No:** `1524`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > jwtGrantByIdentifiableClientsOnly`

198. **File:** `en_test.yaml`, **Line No:** `1529`, **Line Pos:** `21` - **Line No:** `1529`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > jwtGrantEncryptedJwtRejected`

199. **File:** `en_test.yaml`, **Line No:** `1535`, **Line Pos:** `21` - **Line No:** `1535`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > jwtGrantUnsignedJwtRejected`

200. **File:** `en_test.yaml`, **Line No:** `1541`, **Line Pos:** `21` - **Line No:** `1541`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > dcrDuplicateSoftwareIdBlocked`

201. **File:** `en_test.yaml`, **Line No:** `1546`, **Line Pos:** `21` - **Line No:** `1546`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors`

202. **File:** `en_test.yaml`, **Line No:** `1548`, **Line Pos:** `23` - **Line No:** `1548`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors > items`

203. **File:** `en_test.yaml`, **Line No:** `1551`, **Line Pos:** `27` - **Line No:** `1551`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors > items > properties > entityId`

204. **File:** `en_test.yaml`, **Line No:** `1555`, **Line Pos:** `27` - **Line No:** `1555`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > trustAnchors > items > properties > jwks`

205. **File:** `en_test.yaml`, **Line No:** `1566`, **Line Pos:** `21` - **Line No:** `1566`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > openidDroppedOnRefreshWithoutOfflineAccess`

206. **File:** `en_test.yaml`, **Line No:** `1572`, **Line Pos:** `21` - **Line No:** `1572`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsCheckMethods`

207. **File:** `en_test.yaml`, **Line No:** `1574`, **Line Pos:** `23` - **Line No:** `1574`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedDocumentsCheckMethods > items`

208. **File:** `en_test.yaml`, **Line No:** `1580`, **Line Pos:** `21` - **Line No:** `1580`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > rsResponseSigned`

209. **File:** `en_test.yaml`, **Line No:** `1584`, **Line Pos:** `21` - **Line No:** `1584`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > cnonceDuration`

210. **File:** `en_test.yaml`, **Line No:** `1589`, **Line Pos:** `21` - **Line No:** `1589`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > dpopNonceRequired`

211. **File:** `en_test.yaml`, **Line No:** `1594`, **Line Pos:** `21` - **Line No:** `1594`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > verifiableCredentialsEnabled`

212. **File:** `en_test.yaml`, **Line No:** `1599`, **Line Pos:** `21` - **Line No:** `1599`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialJwksUri`

213. **File:** `en_test.yaml`, **Line No:** `1604`, **Line Pos:** `21` - **Line No:** `1604`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialOfferDuration`

214. **File:** `en_test.yaml`, **Line No:** `1609`, **Line Pos:** `21` - **Line No:** `1609`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > dpopNonceDuration`

215. **File:** `en_test.yaml`, **Line No:** `1614`, **Line Pos:** `21` - **Line No:** `1614`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > preAuthorizedGrantAnonymousAccessSupported`

216. **File:** `en_test.yaml`, **Line No:** `1619`, **Line Pos:** `21` - **Line No:** `1619`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialTransactionDuration`

217. **File:** `en_test.yaml`, **Line No:** `1625`, **Line Pos:** `21` - **Line No:** `1625`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > introspectionSignatureKeyId`

218. **File:** `en_test.yaml`, **Line No:** `1629`, **Line Pos:** `21` - **Line No:** `1629`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > resourceSignatureKeyId`

219. **File:** `en_test.yaml`, **Line No:** `1633`, **Line Pos:** `21` - **Line No:** `1633`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > userPinLength`

220. **File:** `en_test.yaml`, **Line No:** `1638`, **Line Pos:** `21` - **Line No:** `1638`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedPromptValues`

221. **File:** `en_test.yaml`, **Line No:** `1640`, **Line Pos:** `23` - **Line No:** `1640`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > supportedPromptValues > items`

222. **File:** `en_test.yaml`, **Line No:** `1655`, **Line Pos:** `21` - **Line No:** `1655`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > idTokenReissuable`

223. **File:** `en_test.yaml`, **Line No:** `1660`, **Line Pos:** `21` - **Line No:** `1660`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialJwks`

224. **File:** `en_test.yaml`, **Line No:** `1665`, **Line Pos:** `21` - **Line No:** `1665`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > fapiModes`

225. **File:** `en_test.yaml`, **Line No:** `1667`, **Line Pos:** `23` - **Line No:** `1667`, **Line Pos:** `24`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > fapiModes > items`

226. **File:** `en_test.yaml`, **Line No:** `1686`, **Line Pos:** `21` - **Line No:** `1686`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialDuration`

227. **File:** `en_test.yaml`, **Line No:** `1691`, **Line Pos:** `21` - **Line No:** `1691`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata`

228. **File:** `en_test.yaml`, **Line No:** `1694`, **Line Pos:** `25` - **Line No:** `1694`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > authorizationServers`

229. **File:** `en_test.yaml`, **Line No:** `1696`, **Line Pos:** `27` - **Line No:** `1696`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > authorizationServers > items`

230. **File:** `en_test.yaml`, **Line No:** `1702`, **Line Pos:** `25` - **Line No:** `1702`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialIssuer`

231. **File:** `en_test.yaml`, **Line No:** `1705`, **Line Pos:** `25` - **Line No:** `1705`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialEndpoint`

232. **File:** `en_test.yaml`, **Line No:** `1708`, **Line Pos:** `25` - **Line No:** `1708`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > batchCredentialEndpoint`

233. **File:** `en_test.yaml`, **Line No:** `1712`, **Line Pos:** `25` - **Line No:** `1712`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > deferredCredentialEndpoint`

234. **File:** `en_test.yaml`, **Line No:** `1715`, **Line Pos:** `25` - **Line No:** `1715`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialsSupported`

235. **File:** `en_test.yaml`, **Line No:** `1718`, **Line Pos:** `25` - **Line No:** `1718`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported`

236. **File:** `en_test.yaml`, **Line No:** `1720`, **Line Pos:** `27` - **Line No:** `1720`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

237. **File:** `en_test.yaml`, **Line No:** `1725`, **Line Pos:** `25` - **Line No:** `1725`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported`

238. **File:** `en_test.yaml`, **Line No:** `1727`, **Line Pos:** `27` - **Line No:** `1727`, **Line Pos:** `28`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

239. **File:** `en_test.yaml`, **Line No:** `1732`, **Line Pos:** `25` - **Line No:** `1732`, **Line Pos:** `26`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > credentialIssuerMetadata > properties > requireCredentialResponseEncryption`

240. **File:** `en_test.yaml`, **Line No:** `1739`, **Line Pos:** `21` - **Line No:** `1739`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > idTokenAudType`

241. **File:** `en_test.yaml`, **Line No:** `1743`, **Line Pos:** `21` - **Line No:** `1743`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 200 > content > application/json > schema > properties > nativeSsoSupported`

242. **File:** `en_test.yaml`, **Line No:** `1866`, **Line Pos:** `21` - **Line No:** `1866`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 400 > content > application/json > schema > properties > resultCode`

243. **File:** `en_test.yaml`, **Line No:** `1869`, **Line Pos:** `21` - **Line No:** `1869`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 400 > content > application/json > schema > properties > resultMessage`

244. **File:** `en_test.yaml`, **Line No:** `1882`, **Line Pos:** `21` - **Line No:** `1882`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 401 > content > application/json > schema > properties > resultCode`

245. **File:** `en_test.yaml`, **Line No:** `1885`, **Line Pos:** `21` - **Line No:** `1885`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 401 > content > application/json > schema > properties > resultMessage`

246. **File:** `en_test.yaml`, **Line No:** `1898`, **Line Pos:** `21` - **Line No:** `1898`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 403 > content > application/json > schema > properties > resultCode`

247. **File:** `en_test.yaml`, **Line No:** `1901`, **Line Pos:** `21` - **Line No:** `1901`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 403 > content > application/json > schema > properties > resultMessage`

248. **File:** `en_test.yaml`, **Line No:** `1914`, **Line Pos:** `21` - **Line No:** `1914`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 500 > content > application/json > schema > properties > resultCode`

249. **File:** `en_test.yaml`, **Line No:** `1917`, **Line Pos:** `21` - **Line No:** `1917`, **Line Pos:** `22`, **Path:** `# > paths > /api/{serviceId}/service/get > get > responses > 500 > content > application/json > schema > properties > resultMessage`

250. **File:** `en_test.yaml`, **Line No:** `1964`, **Line Pos:** `13` - **Line No:** `1964`, **Line Pos:** `14`, **Path:** `# > paths > /api/service/get/list > get > parameters > 0 > schema`

251. **File:** `en_test.yaml`, **Line No:** `1971`, **Line Pos:** `13` - **Line No:** `1971`, **Line Pos:** `14`, **Path:** `# > paths > /api/service/get/list > get > parameters > 1 > schema`

252. **File:** `en_test.yaml`, **Line No:** `1984`, **Line Pos:** `21` - **Line No:** `1984`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > start`

253. **File:** `en_test.yaml`, **Line No:** `1990`, **Line Pos:** `21` - **Line No:** `1990`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > end`

254. **File:** `en_test.yaml`, **Line No:** `1996`, **Line Pos:** `21` - **Line No:** `1996`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > totalCount`

255. **File:** `en_test.yaml`, **Line No:** `2002`, **Line Pos:** `21` - **Line No:** `2002`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services`

256. **File:** `en_test.yaml`, **Line No:** `2004`, **Line Pos:** `23` - **Line No:** `2004`, **Line Pos:** `24`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items`

257. **File:** `en_test.yaml`, **Line No:** `2007`, **Line Pos:** `27` - **Line No:** `2007`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > number`

258. **File:** `en_test.yaml`, **Line No:** `2012`, **Line Pos:** `27` - **Line No:** `2012`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > serviceName`

259. **File:** `en_test.yaml`, **Line No:** `2015`, **Line Pos:** `27` - **Line No:** `2015`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > issuer`

260. **File:** `en_test.yaml`, **Line No:** `2024`, **Line Pos:** `27` - **Line No:** `2024`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > description`

261. **File:** `en_test.yaml`, **Line No:** `2027`, **Line Pos:** `27` - **Line No:** `2027`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > apiKey`

262. **File:** `en_test.yaml`, **Line No:** `2032`, **Line Pos:** `27` - **Line No:** `2032`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > clientIdAliasEnabled`

263. **File:** `en_test.yaml`, **Line No:** `2035`, **Line Pos:** `27` - **Line No:** `2035`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata`

264. **File:** `en_test.yaml`, **Line No:** `2037`, **Line Pos:** `29` - **Line No:** `2037`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata > items`

265. **File:** `en_test.yaml`, **Line No:** `2040`, **Line Pos:** `33` - **Line No:** `2040`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata > items > properties > key`

266. **File:** `en_test.yaml`, **Line No:** `2043`, **Line Pos:** `33` - **Line No:** `2043`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > metadata > items > properties > value`

267. **File:** `en_test.yaml`, **Line No:** `2053`, **Line Pos:** `27` - **Line No:** `2053`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > createdAt`

268. **File:** `en_test.yaml`, **Line No:** `2060`, **Line Pos:** `27` - **Line No:** `2060`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > modifiedAt`

269. **File:** `en_test.yaml`, **Line No:** `2067`, **Line Pos:** `27` - **Line No:** `2067`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authenticationCallbackEndpoint`

270. **File:** `en_test.yaml`, **Line No:** `2078`, **Line Pos:** `27` - **Line No:** `2078`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authenticationCallbackApiKey`

271. **File:** `en_test.yaml`, **Line No:** `2085`, **Line Pos:** `27` - **Line No:** `2085`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authenticationCallbackApiSecret`

272. **File:** `en_test.yaml`, **Line No:** `2088`, **Line Pos:** `27` - **Line No:** `2088`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAcrs`

273. **File:** `en_test.yaml`, **Line No:** `2091`, **Line Pos:** `29` - **Line No:** `2091`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAcrs > items`

274. **File:** `en_test.yaml`, **Line No:** `2098`, **Line Pos:** `27` - **Line No:** `2098`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedGrantTypes`

275. **File:** `en_test.yaml`, **Line No:** `2100`, **Line Pos:** `29` - **Line No:** `2100`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedGrantTypes > items`

276. **File:** `en_test.yaml`, **Line No:** `2119`, **Line Pos:** `27` - **Line No:** `2119`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedResponseTypes`

277. **File:** `en_test.yaml`, **Line No:** `2121`, **Line Pos:** `29` - **Line No:** `2121`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedResponseTypes > items`

278. **File:** `en_test.yaml`, **Line No:** `2138`, **Line Pos:** `27` - **Line No:** `2138`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAuthorizationDetailsTypes`

279. **File:** `en_test.yaml`, **Line No:** `2140`, **Line Pos:** `29` - **Line No:** `2140`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAuthorizationDetailsTypes > items`

280. **File:** `en_test.yaml`, **Line No:** `2147`, **Line Pos:** `27` - **Line No:** `2147`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedServiceProfiles`

281. **File:** `en_test.yaml`, **Line No:** `2149`, **Line Pos:** `29` - **Line No:** `2149`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedServiceProfiles > items`

282. **File:** `en_test.yaml`, **Line No:** `2156`, **Line Pos:** `27` - **Line No:** `2156`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > errorDescriptionOmitted`

283. **File:** `en_test.yaml`, **Line No:** `2165`, **Line Pos:** `27` - **Line No:** `2165`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > errorUriOmitted`

284. **File:** `en_test.yaml`, **Line No:** `2174`, **Line Pos:** `27` - **Line No:** `2174`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authorizationEndpoint`

285. **File:** `en_test.yaml`, **Line No:** `2184`, **Line Pos:** `27` - **Line No:** `2184`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directAuthorizationEndpointEnabled`

286. **File:** `en_test.yaml`, **Line No:** `2190`, **Line Pos:** `27` - **Line No:** `2190`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedUiLocales`

287. **File:** `en_test.yaml`, **Line No:** `2192`, **Line Pos:** `29` - **Line No:** `2192`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedUiLocales > items`

288. **File:** `en_test.yaml`, **Line No:** `2200`, **Line Pos:** `27` - **Line No:** `2200`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDisplays`

289. **File:** `en_test.yaml`, **Line No:** `2202`, **Line Pos:** `29` - **Line No:** `2202`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDisplays > items`

290. **File:** `en_test.yaml`, **Line No:** `2223`, **Line Pos:** `27` - **Line No:** `2223`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > pkceRequired`

291. **File:** `en_test.yaml`, **Line No:** `2231`, **Line Pos:** `27` - **Line No:** `2231`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > pkceS256Required`

292. **File:** `en_test.yaml`, **Line No:** `2239`, **Line Pos:** `27` - **Line No:** `2239`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authorizationResponseDuration`

293. **File:** `en_test.yaml`, **Line No:** `2250`, **Line Pos:** `27` - **Line No:** `2250`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenEndpoint`

294. **File:** `en_test.yaml`, **Line No:** `2260`, **Line Pos:** `27` - **Line No:** `2260`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directTokenEndpointEnabled`

295. **File:** `en_test.yaml`, **Line No:** `2265`, **Line Pos:** `27` - **Line No:** `2265`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTokenAuthMethods`

296. **File:** `en_test.yaml`, **Line No:** `2267`, **Line Pos:** `29` - **Line No:** `2267`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTokenAuthMethods > items`

297. **File:** `en_test.yaml`, **Line No:** `2286`, **Line Pos:** `27` - **Line No:** `2286`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > missingClientIdAllowed`

298. **File:** `en_test.yaml`, **Line No:** `2292`, **Line Pos:** `27` - **Line No:** `2292`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > revocationEndpoint`

299. **File:** `en_test.yaml`, **Line No:** `2299`, **Line Pos:** `27` - **Line No:** `2299`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directRevocationEndpointEnabled`

300. **File:** `en_test.yaml`, **Line No:** `2302`, **Line Pos:** `27` - **Line No:** `2302`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedRevocationAuthMethods`

301. **File:** `en_test.yaml`, **Line No:** `2304`, **Line Pos:** `29` - **Line No:** `2304`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedRevocationAuthMethods > items`

302. **File:** `en_test.yaml`, **Line No:** `2320`, **Line Pos:** `27` - **Line No:** `2320`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > introspectionEndpoint`

303. **File:** `en_test.yaml`, **Line No:** `2324`, **Line Pos:** `27` - **Line No:** `2324`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directIntrospectionEndpointEnabled`

304. **File:** `en_test.yaml`, **Line No:** `2327`, **Line Pos:** `27` - **Line No:** `2327`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIntrospectionAuthMethods`

305. **File:** `en_test.yaml`, **Line No:** `2331`, **Line Pos:** `29` - **Line No:** `2331`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIntrospectionAuthMethods > items`

306. **File:** `en_test.yaml`, **Line No:** `2345`, **Line Pos:** `27` - **Line No:** `2345`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > pushedAuthReqEndpoint`

307. **File:** `en_test.yaml`, **Line No:** `2352`, **Line Pos:** `27` - **Line No:** `2352`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > pushedAuthReqDuration`

308. **File:** `en_test.yaml`, **Line No:** `2366`, **Line Pos:** `27` - **Line No:** `2366`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > parRequired`

309. **File:** `en_test.yaml`, **Line No:** `2374`, **Line Pos:** `27` - **Line No:** `2374`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > requestObjectRequired`

310. **File:** `en_test.yaml`, **Line No:** `2385`, **Line Pos:** `27` - **Line No:** `2385`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > traditionalRequestObjectProcessingApplied`

311. **File:** `en_test.yaml`, **Line No:** `2404`, **Line Pos:** `27` - **Line No:** `2404`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mutualTlsValidatePkiCertChain`

312. **File:** `en_test.yaml`, **Line No:** `2408`, **Line Pos:** `27` - **Line No:** `2408`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustedRootCertificates`

313. **File:** `en_test.yaml`, **Line No:** `2410`, **Line Pos:** `29` - **Line No:** `2410`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustedRootCertificates > items`

314. **File:** `en_test.yaml`, **Line No:** `2414`, **Line Pos:** `27` - **Line No:** `2414`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases`

315. **File:** `en_test.yaml`, **Line No:** `2416`, **Line Pos:** `29` - **Line No:** `2416`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items`

316. **File:** `en_test.yaml`, **Line No:** `2419`, **Line Pos:** `33` - **Line No:** `2419`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items > properties > name`

317. **File:** `en_test.yaml`, **Line No:** `2421`, **Line Pos:** `33` - **Line No:** `2421`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > mtlsEndpointAliases > items > properties > uri`

318. **File:** `en_test.yaml`, **Line No:** `2441`, **Line Pos:** `27` - **Line No:** `2441`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenType`

319. **File:** `en_test.yaml`, **Line No:** `2451`, **Line Pos:** `27` - **Line No:** `2451`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tlsClientCertificateBoundAccessTokens`

320. **File:** `en_test.yaml`, **Line No:** `2455`, **Line Pos:** `27` - **Line No:** `2455`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenDuration`

321. **File:** `en_test.yaml`, **Line No:** `2461`, **Line Pos:** `27` - **Line No:** `2461`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > singleAccessTokenPerSubject`

322. **File:** `en_test.yaml`, **Line No:** `2469`, **Line Pos:** `27` - **Line No:** `2469`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenSignAlg`

323. **File:** `en_test.yaml`, **Line No:** `2495`, **Line Pos:** `27` - **Line No:** `2495`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenSignatureKeyId`

324. **File:** `en_test.yaml`, **Line No:** `2506`, **Line Pos:** `27` - **Line No:** `2506`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > refreshTokenDuration`

325. **File:** `en_test.yaml`, **Line No:** `2510`, **Line Pos:** `27` - **Line No:** `2510`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > refreshTokenDurationKept`

326. **File:** `en_test.yaml`, **Line No:** `2515`, **Line Pos:** `27` - **Line No:** `2515`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > refreshTokenDurationReset`

327. **File:** `en_test.yaml`, **Line No:** `2526`, **Line Pos:** `27` - **Line No:** `2526`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > refreshTokenKept`

328. **File:** `en_test.yaml`, **Line No:** `2534`, **Line Pos:** `27` - **Line No:** `2534`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes`

329. **File:** `en_test.yaml`, **Line No:** `2536`, **Line Pos:** `29` - **Line No:** `2536`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items`

330. **File:** `en_test.yaml`, **Line No:** `2539`, **Line Pos:** `33` - **Line No:** `2539`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > name`

331. **File:** `en_test.yaml`, **Line No:** `2542`, **Line Pos:** `33` - **Line No:** `2542`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > defaultEntry`

332. **File:** `en_test.yaml`, **Line No:** `2545`, **Line Pos:** `33` - **Line No:** `2545`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > description`

333. **File:** `en_test.yaml`, **Line No:** `2548`, **Line Pos:** `33` - **Line No:** `2548`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions`

334. **File:** `en_test.yaml`, **Line No:** `2551`, **Line Pos:** `35` - **Line No:** `2551`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions > items`

335. **File:** `en_test.yaml`, **Line No:** `2554`, **Line Pos:** `39` - **Line No:** `2554`, **Line Pos:** `40`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions > items > properties > tag`

336. **File:** `en_test.yaml`, **Line No:** `2557`, **Line Pos:** `39` - **Line No:** `2557`, **Line Pos:** `40`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > descriptions > items > properties > value`

337. **File:** `en_test.yaml`, **Line No:** `2560`, **Line Pos:** `33` - **Line No:** `2560`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes`

338. **File:** `en_test.yaml`, **Line No:** `2563`, **Line Pos:** `35` - **Line No:** `2563`, **Line Pos:** `36`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes > items`

339. **File:** `en_test.yaml`, **Line No:** `2566`, **Line Pos:** `39` - **Line No:** `2566`, **Line Pos:** `40`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes > items > properties > key`

340. **File:** `en_test.yaml`, **Line No:** `2569`, **Line Pos:** `39` - **Line No:** `2569`, **Line Pos:** `40`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedScopes > items > properties > attributes > items > properties > value`

341. **File:** `en_test.yaml`, **Line No:** `2587`, **Line Pos:** `27` - **Line No:** `2587`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > scopeRequired`

342. **File:** `en_test.yaml`, **Line No:** `2604`, **Line Pos:** `27` - **Line No:** `2604`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > idTokenDuration`

343. **File:** `en_test.yaml`, **Line No:** `2610`, **Line Pos:** `27` - **Line No:** `2610`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > allowableClockSkew`

344. **File:** `en_test.yaml`, **Line No:** `2617`, **Line Pos:** `27` - **Line No:** `2617`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimTypes`

345. **File:** `en_test.yaml`, **Line No:** `2619`, **Line Pos:** `29` - **Line No:** `2619`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimTypes > items`

346. **File:** `en_test.yaml`, **Line No:** `2631`, **Line Pos:** `27` - **Line No:** `2631`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimLocales`

347. **File:** `en_test.yaml`, **Line No:** `2633`, **Line Pos:** `29` - **Line No:** `2633`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaimLocales > items`

348. **File:** `en_test.yaml`, **Line No:** `2642`, **Line Pos:** `27` - **Line No:** `2642`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaims`

349. **File:** `en_test.yaml`, **Line No:** `2644`, **Line Pos:** `29` - **Line No:** `2644`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClaims > items`

350. **File:** `en_test.yaml`, **Line No:** `2677`, **Line Pos:** `27` - **Line No:** `2677`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > claimShortcutRestrictive`

351. **File:** `en_test.yaml`, **Line No:** `2690`, **Line Pos:** `27` - **Line No:** `2690`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > jwksUri`

352. **File:** `en_test.yaml`, **Line No:** `2703`, **Line Pos:** `27` - **Line No:** `2703`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directJwksEndpointEnabled`

353. **File:** `en_test.yaml`, **Line No:** `2708`, **Line Pos:** `27` - **Line No:** `2708`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > jwks`

354. **File:** `en_test.yaml`, **Line No:** `2718`, **Line Pos:** `27` - **Line No:** `2718`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > idTokenSignatureKeyId`

355. **File:** `en_test.yaml`, **Line No:** `2735`, **Line Pos:** `27` - **Line No:** `2735`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userInfoSignatureKeyId`

356. **File:** `en_test.yaml`, **Line No:** `2752`, **Line Pos:** `27` - **Line No:** `2752`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authorizationSignatureKeyId`

357. **File:** `en_test.yaml`, **Line No:** `2768`, **Line Pos:** `27` - **Line No:** `2768`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userInfoEndpoint`

358. **File:** `en_test.yaml`, **Line No:** `2776`, **Line Pos:** `27` - **Line No:** `2776`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > directUserInfoEndpointEnabled`

359. **File:** `en_test.yaml`, **Line No:** `2781`, **Line Pos:** `27` - **Line No:** `2781`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > dynamicRegistrationSupported`

360. **File:** `en_test.yaml`, **Line No:** `2786`, **Line Pos:** `27` - **Line No:** `2786`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > registrationEndpoint`

361. **File:** `en_test.yaml`, **Line No:** `2794`, **Line Pos:** `27` - **Line No:** `2794`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > registrationManagementEndpoint`

362. **File:** `en_test.yaml`, **Line No:** `2802`, **Line Pos:** `27` - **Line No:** `2802`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > policyUri`

363. **File:** `en_test.yaml`, **Line No:** `2809`, **Line Pos:** `27` - **Line No:** `2809`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tosUri`

364. **File:** `en_test.yaml`, **Line No:** `2816`, **Line Pos:** `27` - **Line No:** `2816`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > serviceDocumentation`

365. **File:** `en_test.yaml`, **Line No:** `2823`, **Line Pos:** `27` - **Line No:** `2823`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > backchannelAuthenticationEndpoint`

366. **File:** `en_test.yaml`, **Line No:** `2829`, **Line Pos:** `27` - **Line No:** `2829`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedBackchannelTokenDeliveryModes`

367. **File:** `en_test.yaml`, **Line No:** `2831`, **Line Pos:** `29` - **Line No:** `2831`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedBackchannelTokenDeliveryModes > items`

368. **File:** `en_test.yaml`, **Line No:** `2843`, **Line Pos:** `27` - **Line No:** `2843`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > backchannelAuthReqIdDuration`

369. **File:** `en_test.yaml`, **Line No:** `2850`, **Line Pos:** `27` - **Line No:** `2850`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > backchannelPollingInterval`

370. **File:** `en_test.yaml`, **Line No:** `2857`, **Line Pos:** `27` - **Line No:** `2857`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > backchannelUserCodeParameterSupported`

371. **File:** `en_test.yaml`, **Line No:** `2863`, **Line Pos:** `27` - **Line No:** `2863`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > backchannelBindingMessageRequiredInFapi`

372. **File:** `en_test.yaml`, **Line No:** `2877`, **Line Pos:** `27` - **Line No:** `2877`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > deviceAuthorizationEndpoint`

373. **File:** `en_test.yaml`, **Line No:** `2884`, **Line Pos:** `27` - **Line No:** `2884`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > deviceVerificationUri`

374. **File:** `en_test.yaml`, **Line No:** `2890`, **Line Pos:** `27` - **Line No:** `2890`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > deviceVerificationUriComplete`

375. **File:** `en_test.yaml`, **Line No:** `2908`, **Line Pos:** `27` - **Line No:** `2908`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > deviceFlowCodeDuration`

376. **File:** `en_test.yaml`, **Line No:** `2915`, **Line Pos:** `27` - **Line No:** `2915`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > deviceFlowPollingInterval`

377. **File:** `en_test.yaml`, **Line No:** `2922`, **Line Pos:** `27` - **Line No:** `2922`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userCodeCharset`

378. **File:** `en_test.yaml`, **Line No:** `2929`, **Line Pos:** `27` - **Line No:** `2929`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userCodeLength`

379. **File:** `en_test.yaml`, **Line No:** `2934`, **Line Pos:** `27` - **Line No:** `2934`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTrustFrameworks`

380. **File:** `en_test.yaml`, **Line No:** `2936`, **Line Pos:** `29` - **Line No:** `2936`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedTrustFrameworks > items`

381. **File:** `en_test.yaml`, **Line No:** `2941`, **Line Pos:** `27` - **Line No:** `2941`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedEvidence`

382. **File:** `en_test.yaml`, **Line No:** `2943`, **Line Pos:** `29` - **Line No:** `2943`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedEvidence > items`

383. **File:** `en_test.yaml`, **Line No:** `2947`, **Line Pos:** `27` - **Line No:** `2947`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIdentityDocuments`

384. **File:** `en_test.yaml`, **Line No:** `2949`, **Line Pos:** `29` - **Line No:** `2949`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedIdentityDocuments > items`

385. **File:** `en_test.yaml`, **Line No:** `2954`, **Line Pos:** `27` - **Line No:** `2954`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedVerificationMethods`

386. **File:** `en_test.yaml`, **Line No:** `2956`, **Line Pos:** `29` - **Line No:** `2956`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedVerificationMethods > items`

387. **File:** `en_test.yaml`, **Line No:** `2961`, **Line Pos:** `27` - **Line No:** `2961`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedVerifiedClaims`

388. **File:** `en_test.yaml`, **Line No:** `2963`, **Line Pos:** `29` - **Line No:** `2963`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedVerifiedClaims > items`

389. **File:** `en_test.yaml`, **Line No:** `2968`, **Line Pos:** `27` - **Line No:** `2968`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > verifiedClaimsValidationSchemaSet`

390. **File:** `en_test.yaml`, **Line No:** `2975`, **Line Pos:** `27` - **Line No:** `2975`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes`

391. **File:** `en_test.yaml`, **Line No:** `2977`, **Line Pos:** `29` - **Line No:** `2977`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes > items`

392. **File:** `en_test.yaml`, **Line No:** `2980`, **Line Pos:** `33` - **Line No:** `2980`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes > items > properties > key`

393. **File:** `en_test.yaml`, **Line No:** `2983`, **Line Pos:** `33` - **Line No:** `2983`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > attributes > items > properties > value`

394. **File:** `en_test.yaml`, **Line No:** `2988`, **Line Pos:** `27` - **Line No:** `2988`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > nbfOptional`

395. **File:** `en_test.yaml`, **Line No:** `3011`, **Line Pos:** `27` - **Line No:** `3011`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > issSuppressed`

396. **File:** `en_test.yaml`, **Line No:** `3028`, **Line Pos:** `27` - **Line No:** `3028`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedCustomClientMetadata`

397. **File:** `en_test.yaml`, **Line No:** `3030`, **Line Pos:** `29` - **Line No:** `3030`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedCustomClientMetadata > items`

398. **File:** `en_test.yaml`, **Line No:** `3054`, **Line Pos:** `27` - **Line No:** `3054`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenExpirationLinked`

399. **File:** `en_test.yaml`, **Line No:** `3076`, **Line Pos:** `27` - **Line No:** `3076`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > frontChannelRequestObjectEncryptionRequired`

400. **File:** `en_test.yaml`, **Line No:** `3092`, **Line Pos:** `27` - **Line No:** `3092`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > requestObjectEncryptionAlgMatchRequired`

401. **File:** `en_test.yaml`, **Line No:** `3120`, **Line Pos:** `27` - **Line No:** `3120`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > requestObjectEncryptionEncMatchRequired`

402. **File:** `en_test.yaml`, **Line No:** `3141`, **Line Pos:** `27` - **Line No:** `3141`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsmEnabled`

403. **File:** `en_test.yaml`, **Line No:** `3151`, **Line Pos:** `27` - **Line No:** `3151`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks`

404. **File:** `en_test.yaml`, **Line No:** `3153`, **Line Pos:** `29` - **Line No:** `3153`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items`

405. **File:** `en_test.yaml`, **Line No:** `3158`, **Line Pos:** `33` - **Line No:** `3158`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > kty`

406. **File:** `en_test.yaml`, **Line No:** `3162`, **Line Pos:** `33` - **Line No:** `3162`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > use`

407. **File:** `en_test.yaml`, **Line No:** `3168`, **Line Pos:** `33` - **Line No:** `3168`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > kid`

408. **File:** `en_test.yaml`, **Line No:** `3172`, **Line Pos:** `33` - **Line No:** `3172`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > hsmName`

409. **File:** `en_test.yaml`, **Line No:** `3177`, **Line Pos:** `33` - **Line No:** `3177`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > handle`

410. **File:** `en_test.yaml`, **Line No:** `3182`, **Line Pos:** `33` - **Line No:** `3182`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > publicKey`

411. **File:** `en_test.yaml`, **Line No:** `3186`, **Line Pos:** `33` - **Line No:** `3186`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > hsks > items > properties > alg`

412. **File:** `en_test.yaml`, **Line No:** `3198`, **Line Pos:** `27` - **Line No:** `3198`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > grantManagementEndpoint`

413. **File:** `en_test.yaml`, **Line No:** `3202`, **Line Pos:** `27` - **Line No:** `3202`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > grantManagementActionRequired`

414. **File:** `en_test.yaml`, **Line No:** `3215`, **Line Pos:** `27` - **Line No:** `3215`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > unauthorizedOnClientConfigSupported`

415. **File:** `en_test.yaml`, **Line No:** `3236`, **Line Pos:** `27` - **Line No:** `3236`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > dcrScopeUsedAsRequestable`

416. **File:** `en_test.yaml`, **Line No:** `3247`, **Line Pos:** `27` - **Line No:** `3247`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > endSessionEndpoint`

417. **File:** `en_test.yaml`, **Line No:** `3257`, **Line Pos:** `27` - **Line No:** `3257`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > loopbackRedirectionUriVariable`

418. **File:** `en_test.yaml`, **Line No:** `3299`, **Line Pos:** `27` - **Line No:** `3299`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > requestObjectAudienceChecked`

419. **File:** `en_test.yaml`, **Line No:** `3321`, **Line Pos:** `27` - **Line No:** `3321`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > accessTokenForExternalAttachmentEmbedded`

420. **File:** `en_test.yaml`, **Line No:** `3327`, **Line Pos:** `27` - **Line No:** `3327`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authorityHints`

421. **File:** `en_test.yaml`, **Line No:** `3329`, **Line Pos:** `29` - **Line No:** `3329`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > authorityHints > items`

422. **File:** `en_test.yaml`, **Line No:** `3336`, **Line Pos:** `27` - **Line No:** `3336`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > federationEnabled`

423. **File:** `en_test.yaml`, **Line No:** `3340`, **Line Pos:** `27` - **Line No:** `3340`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > federationJwks`

424. **File:** `en_test.yaml`, **Line No:** `3346`, **Line Pos:** `27` - **Line No:** `3346`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > federationSignatureKeyId`

425. **File:** `en_test.yaml`, **Line No:** `3351`, **Line Pos:** `27` - **Line No:** `3351`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > federationConfigurationDuration`

426. **File:** `en_test.yaml`, **Line No:** `3355`, **Line Pos:** `27` - **Line No:** `3355`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > federationRegistrationEndpoint`

427. **File:** `en_test.yaml`, **Line No:** `3361`, **Line Pos:** `27` - **Line No:** `3361`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > organizationName`

428. **File:** `en_test.yaml`, **Line No:** `3367`, **Line Pos:** `27` - **Line No:** `3367`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > predefinedTransformedClaims`

429. **File:** `en_test.yaml`, **Line No:** `3373`, **Line Pos:** `27` - **Line No:** `3373`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > refreshTokenIdempotent`

430. **File:** `en_test.yaml`, **Line No:** `3380`, **Line Pos:** `27` - **Line No:** `3380`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > signedJwksUri`

431. **File:** `en_test.yaml`, **Line No:** `3386`, **Line Pos:** `27` - **Line No:** `3386`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAttachments`

432. **File:** `en_test.yaml`, **Line No:** `3388`, **Line Pos:** `29` - **Line No:** `3388`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedAttachments > items`

433. **File:** `en_test.yaml`, **Line No:** `3401`, **Line Pos:** `27` - **Line No:** `3401`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDigestAlgorithms`

434. **File:** `en_test.yaml`, **Line No:** `3403`, **Line Pos:** `29` - **Line No:** `3403`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDigestAlgorithms > items`

435. **File:** `en_test.yaml`, **Line No:** `3411`, **Line Pos:** `27` - **Line No:** `3411`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocuments`

436. **File:** `en_test.yaml`, **Line No:** `3413`, **Line Pos:** `29` - **Line No:** `3413`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocuments > items`

437. **File:** `en_test.yaml`, **Line No:** `3418`, **Line Pos:** `27` - **Line No:** `3418`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsMethods`

438. **File:** `en_test.yaml`, **Line No:** `3420`, **Line Pos:** `29` - **Line No:** `3420`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsMethods > items`

439. **File:** `en_test.yaml`, **Line No:** `3431`, **Line Pos:** `27` - **Line No:** `3431`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsValidationMethods`

440. **File:** `en_test.yaml`, **Line No:** `3433`, **Line Pos:** `29` - **Line No:** `3433`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsValidationMethods > items`

441. **File:** `en_test.yaml`, **Line No:** `3440`, **Line Pos:** `27` - **Line No:** `3440`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsVerificationMethods`

442. **File:** `en_test.yaml`, **Line No:** `3442`, **Line Pos:** `29` - **Line No:** `3442`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsVerificationMethods > items`

443. **File:** `en_test.yaml`, **Line No:** `3449`, **Line Pos:** `27` - **Line No:** `3449`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedElectronicRecords`

444. **File:** `en_test.yaml`, **Line No:** `3451`, **Line Pos:** `29` - **Line No:** `3451`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedElectronicRecords > items`

445. **File:** `en_test.yaml`, **Line No:** `3458`, **Line Pos:** `27` - **Line No:** `3458`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClientRegistrationTypes`

446. **File:** `en_test.yaml`, **Line No:** `3460`, **Line Pos:** `29` - **Line No:** `3460`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedClientRegistrationTypes > items`

447. **File:** `en_test.yaml`, **Line No:** `3469`, **Line Pos:** `27` - **Line No:** `3469`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenExchangeByIdentifiableClientsOnly`

448. **File:** `en_test.yaml`, **Line No:** `3474`, **Line Pos:** `27` - **Line No:** `3474`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenExchangeByConfidentialClientsOnly`

449. **File:** `en_test.yaml`, **Line No:** `3479`, **Line Pos:** `27` - **Line No:** `3479`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenExchangeByPermittedClientsOnly`

450. **File:** `en_test.yaml`, **Line No:** `3484`, **Line Pos:** `27` - **Line No:** `3484`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenExchangeEncryptedJwtRejected`

451. **File:** `en_test.yaml`, **Line No:** `3489`, **Line Pos:** `27` - **Line No:** `3489`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > tokenExchangeUnsignedJwtRejected`

452. **File:** `en_test.yaml`, **Line No:** `3494`, **Line Pos:** `27` - **Line No:** `3494`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > jwtGrantByIdentifiableClientsOnly`

453. **File:** `en_test.yaml`, **Line No:** `3499`, **Line Pos:** `27` - **Line No:** `3499`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > jwtGrantEncryptedJwtRejected`

454. **File:** `en_test.yaml`, **Line No:** `3505`, **Line Pos:** `27` - **Line No:** `3505`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > jwtGrantUnsignedJwtRejected`

455. **File:** `en_test.yaml`, **Line No:** `3511`, **Line Pos:** `27` - **Line No:** `3511`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > dcrDuplicateSoftwareIdBlocked`

456. **File:** `en_test.yaml`, **Line No:** `3516`, **Line Pos:** `27` - **Line No:** `3516`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors`

457. **File:** `en_test.yaml`, **Line No:** `3518`, **Line Pos:** `29` - **Line No:** `3518`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors > items`

458. **File:** `en_test.yaml`, **Line No:** `3521`, **Line Pos:** `33` - **Line No:** `3521`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors > items > properties > entityId`

459. **File:** `en_test.yaml`, **Line No:** `3525`, **Line Pos:** `33` - **Line No:** `3525`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > trustAnchors > items > properties > jwks`

460. **File:** `en_test.yaml`, **Line No:** `3536`, **Line Pos:** `27` - **Line No:** `3536`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > openidDroppedOnRefreshWithoutOfflineAccess`

461. **File:** `en_test.yaml`, **Line No:** `3542`, **Line Pos:** `27` - **Line No:** `3542`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsCheckMethods`

462. **File:** `en_test.yaml`, **Line No:** `3544`, **Line Pos:** `29` - **Line No:** `3544`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedDocumentsCheckMethods > items`

463. **File:** `en_test.yaml`, **Line No:** `3550`, **Line Pos:** `27` - **Line No:** `3550`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > rsResponseSigned`

464. **File:** `en_test.yaml`, **Line No:** `3554`, **Line Pos:** `27` - **Line No:** `3554`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > cnonceDuration`

465. **File:** `en_test.yaml`, **Line No:** `3559`, **Line Pos:** `27` - **Line No:** `3559`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > dpopNonceRequired`

466. **File:** `en_test.yaml`, **Line No:** `3564`, **Line Pos:** `27` - **Line No:** `3564`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > verifiableCredentialsEnabled`

467. **File:** `en_test.yaml`, **Line No:** `3569`, **Line Pos:** `27` - **Line No:** `3569`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialJwksUri`

468. **File:** `en_test.yaml`, **Line No:** `3574`, **Line Pos:** `27` - **Line No:** `3574`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialOfferDuration`

469. **File:** `en_test.yaml`, **Line No:** `3579`, **Line Pos:** `27` - **Line No:** `3579`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > dpopNonceDuration`

470. **File:** `en_test.yaml`, **Line No:** `3584`, **Line Pos:** `27` - **Line No:** `3584`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > preAuthorizedGrantAnonymousAccessSupported`

471. **File:** `en_test.yaml`, **Line No:** `3589`, **Line Pos:** `27` - **Line No:** `3589`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialTransactionDuration`

472. **File:** `en_test.yaml`, **Line No:** `3595`, **Line Pos:** `27` - **Line No:** `3595`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > introspectionSignatureKeyId`

473. **File:** `en_test.yaml`, **Line No:** `3599`, **Line Pos:** `27` - **Line No:** `3599`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > resourceSignatureKeyId`

474. **File:** `en_test.yaml`, **Line No:** `3603`, **Line Pos:** `27` - **Line No:** `3603`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > userPinLength`

475. **File:** `en_test.yaml`, **Line No:** `3608`, **Line Pos:** `27` - **Line No:** `3608`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedPromptValues`

476. **File:** `en_test.yaml`, **Line No:** `3610`, **Line Pos:** `29` - **Line No:** `3610`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > supportedPromptValues > items`

477. **File:** `en_test.yaml`, **Line No:** `3625`, **Line Pos:** `27` - **Line No:** `3625`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > idTokenReissuable`

478. **File:** `en_test.yaml`, **Line No:** `3630`, **Line Pos:** `27` - **Line No:** `3630`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialJwks`

479. **File:** `en_test.yaml`, **Line No:** `3635`, **Line Pos:** `27` - **Line No:** `3635`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > fapiModes`

480. **File:** `en_test.yaml`, **Line No:** `3637`, **Line Pos:** `29` - **Line No:** `3637`, **Line Pos:** `30`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > fapiModes > items`

481. **File:** `en_test.yaml`, **Line No:** `3656`, **Line Pos:** `27` - **Line No:** `3656`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialDuration`

482. **File:** `en_test.yaml`, **Line No:** `3661`, **Line Pos:** `27` - **Line No:** `3661`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata`

483. **File:** `en_test.yaml`, **Line No:** `3664`, **Line Pos:** `31` - **Line No:** `3664`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > authorizationServers`

484. **File:** `en_test.yaml`, **Line No:** `3666`, **Line Pos:** `33` - **Line No:** `3666`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > authorizationServers > items`

485. **File:** `en_test.yaml`, **Line No:** `3672`, **Line Pos:** `31` - **Line No:** `3672`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialIssuer`

486. **File:** `en_test.yaml`, **Line No:** `3675`, **Line Pos:** `31` - **Line No:** `3675`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialEndpoint`

487. **File:** `en_test.yaml`, **Line No:** `3678`, **Line Pos:** `31` - **Line No:** `3678`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > batchCredentialEndpoint`

488. **File:** `en_test.yaml`, **Line No:** `3682`, **Line Pos:** `31` - **Line No:** `3682`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > deferredCredentialEndpoint`

489. **File:** `en_test.yaml`, **Line No:** `3685`, **Line Pos:** `31` - **Line No:** `3685`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialsSupported`

490. **File:** `en_test.yaml`, **Line No:** `3688`, **Line Pos:** `31` - **Line No:** `3688`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported`

491. **File:** `en_test.yaml`, **Line No:** `3690`, **Line Pos:** `33` - **Line No:** `3690`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionAlgValuesSupported > items`

492. **File:** `en_test.yaml`, **Line No:** `3695`, **Line Pos:** `31` - **Line No:** `3695`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported`

493. **File:** `en_test.yaml`, **Line No:** `3697`, **Line Pos:** `33` - **Line No:** `3697`, **Line Pos:** `34`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > credentialResponseEncryptionEncValuesSupported > items`

494. **File:** `en_test.yaml`, **Line No:** `3702`, **Line Pos:** `31` - **Line No:** `3702`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > credentialIssuerMetadata > properties > requireCredentialResponseEncryption`

495. **File:** `en_test.yaml`, **Line No:** `3709`, **Line Pos:** `27` - **Line No:** `3709`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > idTokenAudType`

496. **File:** `en_test.yaml`, **Line No:** `3713`, **Line Pos:** `27` - **Line No:** `3713`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/get/list > get > responses > 200 > content > application/json > schema > properties > services > items > properties > nativeSsoSupported`

497. **File:** `en_test.yaml`, **Line No:** `3846`, **Line Pos:** `21` - **Line No:** `3846`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 400 > content > application/json > schema > properties > resultCode`

498. **File:** `en_test.yaml`, **Line No:** `3849`, **Line Pos:** `21` - **Line No:** `3849`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 400 > content > application/json > schema > properties > resultMessage`

499. **File:** `en_test.yaml`, **Line No:** `3862`, **Line Pos:** `21` - **Line No:** `3862`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 401 > content > application/json > schema > properties > resultCode`

500. **File:** `en_test.yaml`, **Line No:** `3865`, **Line Pos:** `21` - **Line No:** `3865`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 401 > content > application/json > schema > properties > resultMessage`

501. **File:** `en_test.yaml`, **Line No:** `3878`, **Line Pos:** `21` - **Line No:** `3878`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 403 > content > application/json > schema > properties > resultCode`

502. **File:** `en_test.yaml`, **Line No:** `3881`, **Line Pos:** `21` - **Line No:** `3881`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 403 > content > application/json > schema > properties > resultMessage`

503. **File:** `en_test.yaml`, **Line No:** `3894`, **Line Pos:** `21` - **Line No:** `3894`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 500 > content > application/json > schema > properties > resultCode`

504. **File:** `en_test.yaml`, **Line No:** `3897`, **Line Pos:** `21` - **Line No:** `3897`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/get/list > get > responses > 500 > content > application/json > schema > properties > resultMessage`

505. **File:** `en_test.yaml`, **Line No:** `3943`, **Line Pos:** `19` - **Line No:** `3943`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > number`

506. **File:** `en_test.yaml`, **Line No:** `3948`, **Line Pos:** `19` - **Line No:** `3948`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > serviceName`

507. **File:** `en_test.yaml`, **Line No:** `3951`, **Line Pos:** `19` - **Line No:** `3951`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > issuer`

508. **File:** `en_test.yaml`, **Line No:** `3960`, **Line Pos:** `19` - **Line No:** `3960`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > description`

509. **File:** `en_test.yaml`, **Line No:** `3963`, **Line Pos:** `19` - **Line No:** `3963`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > apiKey`

510. **File:** `en_test.yaml`, **Line No:** `3968`, **Line Pos:** `19` - **Line No:** `3968`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > clientIdAliasEnabled`

511. **File:** `en_test.yaml`, **Line No:** `3971`, **Line Pos:** `19` - **Line No:** `3971`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata`

512. **File:** `en_test.yaml`, **Line No:** `3973`, **Line Pos:** `21` - **Line No:** `3973`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata > items`

513. **File:** `en_test.yaml`, **Line No:** `3976`, **Line Pos:** `25` - **Line No:** `3976`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata > items > properties > key`

514. **File:** `en_test.yaml`, **Line No:** `3979`, **Line Pos:** `25` - **Line No:** `3979`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > metadata > items > properties > value`

515. **File:** `en_test.yaml`, **Line No:** `3989`, **Line Pos:** `19` - **Line No:** `3989`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > createdAt`

516. **File:** `en_test.yaml`, **Line No:** `3996`, **Line Pos:** `19` - **Line No:** `3996`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > modifiedAt`

517. **File:** `en_test.yaml`, **Line No:** `4003`, **Line Pos:** `19` - **Line No:** `4003`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authenticationCallbackEndpoint`

518. **File:** `en_test.yaml`, **Line No:** `4014`, **Line Pos:** `19` - **Line No:** `4014`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authenticationCallbackApiKey`

519. **File:** `en_test.yaml`, **Line No:** `4021`, **Line Pos:** `19` - **Line No:** `4021`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authenticationCallbackApiSecret`

520. **File:** `en_test.yaml`, **Line No:** `4024`, **Line Pos:** `19` - **Line No:** `4024`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAcrs`

521. **File:** `en_test.yaml`, **Line No:** `4027`, **Line Pos:** `21` - **Line No:** `4027`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAcrs > items`

522. **File:** `en_test.yaml`, **Line No:** `4034`, **Line Pos:** `19` - **Line No:** `4034`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedGrantTypes`

523. **File:** `en_test.yaml`, **Line No:** `4036`, **Line Pos:** `21` - **Line No:** `4036`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedGrantTypes > items`

524. **File:** `en_test.yaml`, **Line No:** `4055`, **Line Pos:** `19` - **Line No:** `4055`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedResponseTypes`

525. **File:** `en_test.yaml`, **Line No:** `4057`, **Line Pos:** `21` - **Line No:** `4057`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedResponseTypes > items`

526. **File:** `en_test.yaml`, **Line No:** `4074`, **Line Pos:** `19` - **Line No:** `4074`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAuthorizationDetailsTypes`

527. **File:** `en_test.yaml`, **Line No:** `4076`, **Line Pos:** `21` - **Line No:** `4076`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedAuthorizationDetailsTypes > items`

528. **File:** `en_test.yaml`, **Line No:** `4083`, **Line Pos:** `19` - **Line No:** `4083`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedServiceProfiles`

529. **File:** `en_test.yaml`, **Line No:** `4085`, **Line Pos:** `21` - **Line No:** `4085`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedServiceProfiles > items`

530. **File:** `en_test.yaml`, **Line No:** `4092`, **Line Pos:** `19` - **Line No:** `4092`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > errorDescriptionOmitted`

531. **File:** `en_test.yaml`, **Line No:** `4101`, **Line Pos:** `19` - **Line No:** `4101`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > errorUriOmitted`

532. **File:** `en_test.yaml`, **Line No:** `4110`, **Line Pos:** `19` - **Line No:** `4110`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authorizationEndpoint`

533. **File:** `en_test.yaml`, **Line No:** `4120`, **Line Pos:** `19` - **Line No:** `4120`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directAuthorizationEndpointEnabled`

534. **File:** `en_test.yaml`, **Line No:** `4126`, **Line Pos:** `19` - **Line No:** `4126`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedUiLocales`

535. **File:** `en_test.yaml`, **Line No:** `4128`, **Line Pos:** `21` - **Line No:** `4128`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedUiLocales > items`

536. **File:** `en_test.yaml`, **Line No:** `4136`, **Line Pos:** `19` - **Line No:** `4136`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDisplays`

537. **File:** `en_test.yaml`, **Line No:** `4138`, **Line Pos:** `21` - **Line No:** `4138`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedDisplays > items`

538. **File:** `en_test.yaml`, **Line No:** `4159`, **Line Pos:** `19` - **Line No:** `4159`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > pkceRequired`

539. **File:** `en_test.yaml`, **Line No:** `4167`, **Line Pos:** `19` - **Line No:** `4167`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > pkceS256Required`

540. **File:** `en_test.yaml`, **Line No:** `4175`, **Line Pos:** `19` - **Line No:** `4175`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authorizationResponseDuration`

541. **File:** `en_test.yaml`, **Line No:** `4186`, **Line Pos:** `19` - **Line No:** `4186`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > tokenEndpoint`

542. **File:** `en_test.yaml`, **Line No:** `4196`, **Line Pos:** `19` - **Line No:** `4196`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directTokenEndpointEnabled`

543. **File:** `en_test.yaml`, **Line No:** `4201`, **Line Pos:** `19` - **Line No:** `4201`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedTokenAuthMethods`

544. **File:** `en_test.yaml`, **Line No:** `4203`, **Line Pos:** `21` - **Line No:** `4203`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedTokenAuthMethods > items`

545. **File:** `en_test.yaml`, **Line No:** `4222`, **Line Pos:** `19` - **Line No:** `4222`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > missingClientIdAllowed`

546. **File:** `en_test.yaml`, **Line No:** `4228`, **Line Pos:** `19` - **Line No:** `4228`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > revocationEndpoint`

547. **File:** `en_test.yaml`, **Line No:** `4235`, **Line Pos:** `19` - **Line No:** `4235`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directRevocationEndpointEnabled`

548. **File:** `en_test.yaml`, **Line No:** `4238`, **Line Pos:** `19` - **Line No:** `4238`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedRevocationAuthMethods`

549. **File:** `en_test.yaml`, **Line No:** `4240`, **Line Pos:** `21` - **Line No:** `4240`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedRevocationAuthMethods > items`

550. **File:** `en_test.yaml`, **Line No:** `4256`, **Line Pos:** `19` - **Line No:** `4256`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > introspectionEndpoint`

551. **File:** `en_test.yaml`, **Line No:** `4260`, **Line Pos:** `19` - **Line No:** `4260`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directIntrospectionEndpointEnabled`

552. **File:** `en_test.yaml`, **Line No:** `4263`, **Line Pos:** `19` - **Line No:** `4263`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedIntrospectionAuthMethods`

553. **File:** `en_test.yaml`, **Line No:** `4267`, **Line Pos:** `21` - **Line No:** `4267`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedIntrospectionAuthMethods > items`

554. **File:** `en_test.yaml`, **Line No:** `4281`, **Line Pos:** `19` - **Line No:** `4281`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > pushedAuthReqEndpoint`

555. **File:** `en_test.yaml`, **Line No:** `4288`, **Line Pos:** `19` - **Line No:** `4288`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > pushedAuthReqDuration`

556. **File:** `en_test.yaml`, **Line No:** `4302`, **Line Pos:** `19` - **Line No:** `4302`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > parRequired`

557. **File:** `en_test.yaml`, **Line No:** `4310`, **Line Pos:** `19` - **Line No:** `4310`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > requestObjectRequired`

558. **File:** `en_test.yaml`, **Line No:** `4321`, **Line Pos:** `19` - **Line No:** `4321`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > traditionalRequestObjectProcessingApplied`

559. **File:** `en_test.yaml`, **Line No:** `4340`, **Line Pos:** `19` - **Line No:** `4340`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mutualTlsValidatePkiCertChain`

560. **File:** `en_test.yaml`, **Line No:** `4344`, **Line Pos:** `19` - **Line No:** `4344`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > trustedRootCertificates`

561. **File:** `en_test.yaml`, **Line No:** `4346`, **Line Pos:** `21` - **Line No:** `4346`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > trustedRootCertificates > items`

562. **File:** `en_test.yaml`, **Line No:** `4350`, **Line Pos:** `19` - **Line No:** `4350`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases`

563. **File:** `en_test.yaml`, **Line No:** `4352`, **Line Pos:** `21` - **Line No:** `4352`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items`

564. **File:** `en_test.yaml`, **Line No:** `4355`, **Line Pos:** `25` - **Line No:** `4355`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > name`

565. **File:** `en_test.yaml`, **Line No:** `4357`, **Line Pos:** `25` - **Line No:** `4357`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > mtlsEndpointAliases > items > properties > uri`

566. **File:** `en_test.yaml`, **Line No:** `4377`, **Line Pos:** `19` - **Line No:** `4377`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > accessTokenType`

567. **File:** `en_test.yaml`, **Line No:** `4387`, **Line Pos:** `19` - **Line No:** `4387`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > tlsClientCertificateBoundAccessTokens`

568. **File:** `en_test.yaml`, **Line No:** `4391`, **Line Pos:** `19` - **Line No:** `4391`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > accessTokenDuration`

569. **File:** `en_test.yaml`, **Line No:** `4397`, **Line Pos:** `19` - **Line No:** `4397`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > singleAccessTokenPerSubject`

570. **File:** `en_test.yaml`, **Line No:** `4405`, **Line Pos:** `19` - **Line No:** `4405`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > accessTokenSignAlg`

571. **File:** `en_test.yaml`, **Line No:** `4431`, **Line Pos:** `19` - **Line No:** `4431`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > accessTokenSignatureKeyId`

572. **File:** `en_test.yaml`, **Line No:** `4442`, **Line Pos:** `19` - **Line No:** `4442`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > refreshTokenDuration`

573. **File:** `en_test.yaml`, **Line No:** `4446`, **Line Pos:** `19` - **Line No:** `4446`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > refreshTokenDurationKept`

574. **File:** `en_test.yaml`, **Line No:** `4451`, **Line Pos:** `19` - **Line No:** `4451`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > refreshTokenDurationReset`

575. **File:** `en_test.yaml`, **Line No:** `4462`, **Line Pos:** `19` - **Line No:** `4462`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > refreshTokenKept`

576. **File:** `en_test.yaml`, **Line No:** `4470`, **Line Pos:** `19` - **Line No:** `4470`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes`

577. **File:** `en_test.yaml`, **Line No:** `4472`, **Line Pos:** `21` - **Line No:** `4472`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items`

578. **File:** `en_test.yaml`, **Line No:** `4475`, **Line Pos:** `25` - **Line No:** `4475`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > name`

579. **File:** `en_test.yaml`, **Line No:** `4478`, **Line Pos:** `25` - **Line No:** `4478`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > defaultEntry`

580. **File:** `en_test.yaml`, **Line No:** `4481`, **Line Pos:** `25` - **Line No:** `4481`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > description`

581. **File:** `en_test.yaml`, **Line No:** `4484`, **Line Pos:** `25` - **Line No:** `4484`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions`

582. **File:** `en_test.yaml`, **Line No:** `4487`, **Line Pos:** `27` - **Line No:** `4487`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items`

583. **File:** `en_test.yaml`, **Line No:** `4490`, **Line Pos:** `31` - **Line No:** `4490`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items > properties > tag`

584. **File:** `en_test.yaml`, **Line No:** `4493`, **Line Pos:** `31` - **Line No:** `4493`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > descriptions > items > properties > value`

585. **File:** `en_test.yaml`, **Line No:** `4496`, **Line Pos:** `25` - **Line No:** `4496`, **Line Pos:** `26`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes`

586. **File:** `en_test.yaml`, **Line No:** `4499`, **Line Pos:** `27` - **Line No:** `4499`, **Line Pos:** `28`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items`

587. **File:** `en_test.yaml`, **Line No:** `4502`, **Line Pos:** `31` - **Line No:** `4502`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items > properties > key`

588. **File:** `en_test.yaml`, **Line No:** `4505`, **Line Pos:** `31` - **Line No:** `4505`, **Line Pos:** `32`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedScopes > items > properties > attributes > items > properties > value`

589. **File:** `en_test.yaml`, **Line No:** `4523`, **Line Pos:** `19` - **Line No:** `4523`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > scopeRequired`

590. **File:** `en_test.yaml`, **Line No:** `4540`, **Line Pos:** `19` - **Line No:** `4540`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > idTokenDuration`

591. **File:** `en_test.yaml`, **Line No:** `4546`, **Line Pos:** `19` - **Line No:** `4546`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > allowableClockSkew`

592. **File:** `en_test.yaml`, **Line No:** `4553`, **Line Pos:** `19` - **Line No:** `4553`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimTypes`

593. **File:** `en_test.yaml`, **Line No:** `4555`, **Line Pos:** `21` - **Line No:** `4555`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimTypes > items`

594. **File:** `en_test.yaml`, **Line No:** `4567`, **Line Pos:** `19` - **Line No:** `4567`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimLocales`

595. **File:** `en_test.yaml`, **Line No:** `4569`, **Line Pos:** `21` - **Line No:** `4569`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaimLocales > items`

596. **File:** `en_test.yaml`, **Line No:** `4578`, **Line Pos:** `19` - **Line No:** `4578`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaims`

597. **File:** `en_test.yaml`, **Line No:** `4580`, **Line Pos:** `21` - **Line No:** `4580`, **Line Pos:** `22`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > supportedClaims > items`

598. **File:** `en_test.yaml`, **Line No:** `4613`, **Line Pos:** `19` - **Line No:** `4613`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > claimShortcutRestrictive`

599. **File:** `en_test.yaml`, **Line No:** `4626`, **Line Pos:** `19` - **Line No:** `4626`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > jwksUri`

600. **File:** `en_test.yaml`, **Line No:** `4639`, **Line Pos:** `19` - **Line No:** `4639`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > directJwksEndpointEnabled`

601. **File:** `en_test.yaml`, **Line No:** `4644`, **Line Pos:** `19` - **Line No:** `4644`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > jwks`

602. **File:** `en_test.yaml`, **Line No:** `4654`, **Line Pos:** `19` - **Line No:** `4654`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > idTokenSignatureKeyId`

603. **File:** `en_test.yaml`, **Line No:** `4671`, **Line Pos:** `19` - **Line No:** `4671`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > userInfoSignatureKeyId`

604. **File:** `en_test.yaml`, **Line No:** `4688`, **Line Pos:** `19` - **Line No:** `4688`, **Line Pos:** `20`, **Path:** `# > paths > /api/service/create > post > requestBody > content > application/json > schema > properties > authorizationSignatureKeyId`




