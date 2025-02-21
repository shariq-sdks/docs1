# Basic Structure

## [./app](./app) directory

This directory contains all the application files to be deployed.

## [./app/specs](./app/specs) directory

```
.
└── app
    └── specs
        ├── shared
        │   ├── 2.2.19
        │   │   ├── en.yaml
        |   |   ...
        │   ├── 2.2.25
        │   │   |── en.yaml
        |   |   ...
        |   ...
        ├── dedicated
        │   ├── ...
        |   ...
        └── onpremise
        │   ├── ...
        │   ...
        ...
```

This directory contains the bundled API specification files to be referenced by the deployed application.

A bundled specification file in this directory is an Open API specification file that describes a specific **server-type** and a specific **version** of Authlete APIs in a specific **language**. For example, `shared/3.0.0/en.yaml` is an Open API specification file that describes Authlete **3.0.0** in the **shared** environment in **English**.

The relative path of the bundled files in this directory must follow the `{server_type}/{version}/{locale}.yaml` structure.

**WARNING**: You **SHOULD NOT** manually modify files in this directory. All of those modifications should be done using the `swagger-cli` command. See [How To Update](#how-to-update) for more details.

## [./app/config.js](./app/config.js)

This file contains the main configuration settings for the application. Here are the properties you can configure in this file.

| **Property**           | **Description**                                                    | **Value Type**      | **Example Values**                                     |
|------------------------|--------------------------------------------------------------------|---------------------|--------------------------------------------------------|
| `supportedLocales`     | List of supported application locales.                             | `array of strings`  | `[ 'en', 'ja' ]`                                       |
| `defaultLocale`        | Default locale when none is specified.                             | `string`            | `'en'`                                                 |
| `supportedServerTypes` | Types of servers supported by the application.                     | `array of strings`  | `[ 'shared', 'dedicated' ]`                            |
| `supportedVersions`    | API documentation versions supported per server type.              | `object`            | `{ shared: ['2.3.0', '3.0.0'], dedicated: ['2.3.0'] }` |
| `defaultPath`          | URL path users are redirected to when accessing the root path `/`. | `string`            | `'/en/shared/latest'`                                  |
| `port`                 | Port on which the application runs.                                | `number`            | `8080`                                                 |
| `credentials`          | Authentication details for accessing protected resources.          | `object`            | `{ shared: { username: 'user', password: 'pass' } }`   |
| `isProduction`         | Indicates whether the app is running in production mode.           | `boolean`           | `true`                                                 |
| `logLevel`             | Sets the application log level.                                    | `string`            | `'info'`                                               |
| `logDestination`       | Destination for log output.                                        | `string`            | `/var/log/app.log`                                     |

## [./specs](./specs) directory

```
.
└── specs
    ├── shared
    │   ├── 2.2.19
    │   │   └── en
    │   │   │   ├── authlete-api.yml
    |   │   │   ...
    │   │   ...
    │   ├── 2.2.25
    │   │   └── en
    │   │   |   ├── authlete-api.yml
    |   |   │   ...
    │   │   ...
    │   ...
    ├── dedicated
    │   ├── ...
    |   ...
    └── onpremise
    │   ├── ...
    │   ...
    ...
```

This directory exists for maintaining the API documentation. If you want to add/edit API documentation contents, make changes to the files in this directory. And then, bundle the target files and add the bundled file to the contents in [./app/specs](./app/specs) using the `swagger-cli` command. See [How To Update](#how-to-update) for more details.

NOTE: Even if you make changes to the contents in this directory, the changes won't be reflected in the application unless you apply them in [./app/specs](./app/specs).

---

# How To Run

```shell
# Move to the app directory.
$ cd app

# Get the app running.
$ docker-compose up
```

---

# How To Update

1. Make changes to files in [./specs](./specs) directory.

2. Use the `swagger-cli` command as shown below to bundle the contents in [./specs](./specs) directory and output the bundled file in [./app/specs](./app/specs).

NOTE: The bundled file must be outputted as `./app/spec/{server_type}/{version}/{locale}.yaml`.

```shell
# Bundle API specification files in 'specs/shared/3.0.0/en' directory and output
# it as 'app/specs/shared/3.0.0/en.yaml'.
$ swagger-cli bundle -f yaml \
-o app/specs/shared/3.0.0/en.yaml \
specs/shared/3.0.0/en/authlete-api.yaml
```

3. Update configuration properties in [./app/config.js](./app/config.js) (e.g.`supportedVersions`, `supportedLocales`) if necessary.

4. Test locally.

5. Commit the changes and push them to the repository.

NOTE: Merging commits into the master branch automatically triggers application deployment.
