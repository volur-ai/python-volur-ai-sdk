# Getting started

Völur SDK is a Python package that provides a simple interface for
interacting with the Völur products and services. It is designed to be easy to
use and integrate seamlessly with your existing development workflow.

## What is Völur SDK?

Völur SDK helps you to integrate with the Völur API. At the moment,
the core functionality of the SDK is to provide a simple interface for
uploading the data to the Völur platform.

## Völur SDK Model

The Völur SDK is based on the following model:

- **Client**: the main entry point for your application. It provides a
  simple interface for interacting with the Völur API.
- **Endpoints**: a set of different endpoints that you can use to interact
  with the Völur API.
- **Sources**: a set of different sources that you can use to upload data
  to the Völur platform.

## How can I use the SDK?

This libray is designed to seamlessly integrate with your existing development
workflow. It's typed and tested. We deliver the library with namespaced
packages to keep backward compatibility as long as you need.

For installation instructions, please refer to the [Installation][installation].

[installation]: installation.md

Once library is installed, you can start using it by importing the client and
providing [the necessary credentials][authentication].

[authentication]: authentication.md

!!! note "Obtain credentials from Volur developers"
    To use the Völur SDK, you need to obtain the necessary credentials from
    the Volur developers. Please contact us to get the credentials.

```python title="example.py" linenums="1"
from volur.sdk.client import VolurClient

client = VolurClient()
```

See the list of available methods in the [API Reference][api-reference]
of Volur Client or take a look at the [examples][examples].

[api-reference]: http://127.0.0.1:8000/reference/volur/sdk/#volur.sdk.VolurClient
[examples]: examples/index.md
