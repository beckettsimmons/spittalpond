Config Interface Usage
======================

Introduction
------------
The Spittalpond config interface was created to automatically, quickly, and
consistently call the Oasis Django API calls by parsing a pre-written
configuration file.

The Oasis Django API is very flexible and has over 300 different calls that can
be made and each call must be made in a specific order. This makes running
Oasis models and generating output data rather tedious and easy to call
webservices in the incorrect order.

Spittalpond begins to address this issues by grouping API calls into logical
chunks. Though this still may mean that you have to **manually** make, say, ten
or so Spittalpond calls instead.

This is why Spittalpond goes another step further and has a config interface to
make running Oasis quick and easy. This means that all you need to do is write
a configuration file once and then be able to run Oasis with just one Python
command! Great, right?!

What is TOML?
-------------
TOML stands for Tom's Obviously Minimal Language.
The TOML data format is much like the classic `.ini` format though it adds more
features and functionality, (for example, nested sections and better lists)

TOML mainly uses basic sections, and key-value pairs to define and structure
data and is very easy to use and understand. For those of us familiar with
JSON, we can think of TOML as just gloried human readable JSON.

For example, this TOML::

    [person]
    first_name = "John"
    last_name = "Doe"
    hobbies = ["walking", "skipping", "jumping"]
    alive = true

Is the JSON equivalent of::

    {"person":
        {"first_name":"John",
        "last_name":"Doe",
        "hobbies":["walkin", "skipping", "jumping"]
        "alive": true
        }
    }

To learn more about the TOML specification, click here_.

Spittalpond Config Specification
--------------------------------
In order for TOML configuration files to be usable by Spittalpond their data
structure must follow this specification.

An file named example.toml_ is provided as a reference example of how a
Spittalpond configuration file should look. It also contains many useful
comments and pro-tips. As we can see, this file is separated into different
logical sections of the Oasis workflow defined in the *Oasis User Guide R1.2
v1.0*[1].

Essentially, each section conveniently runs many underlying Oasis webservices.
Each section specified in the configuration file will be run based on key value
pairs and sub-sections defined in it. The sections will be run in an order
defined by Spittalpond. This means that we need not worry about the order in
the TOML file. All sections defined in the configuration file will be run.

Following is a brief description of each section in example.toml:

**meta**
The meta section defines Spittalpond data and initializations, not any Oasis
specific data.

The key-value pairs in Meta are:

- url: which holds the Oasis url.
- log_file: which holds the name of the log file.
- log_level: allows the user to specify levels of logging.
- system_config: contains the value of the Oasis back-end database to be used for execution.

**Login**

Login section is an optional section. Key-value pairs in Login are:
user: contains the username to access Oasis.
password: password to access Oasis.

directory_path: holds the path of the directory containing input files to be
uploaded on Oasis.

**Model**

Model section defines essential details of the model to be created. Key-value pairs
in Model section are:

- name: defines the name of the Model to be created on Oasis.
- do_timestamps: defines timestamps for the upload files. This sub-section, allows
  the user to either turn it on to be used or turn it off.
- key: defines the license key for the Model.

There are seven main model sections to load the models into Oasis:

- model.dict.areaperil
- model.dict.event
- model.dict.vuln
- model.dict.hazardintensitybin
- model.version.hazfp
- model.version.vuln
- model.dict.damagebin

All the above sections have two key-value pairs:

- filename: defines the name of the input file to be uploaded.
- module_supplier_id: defines module supplier id.

**Exposure**

Exposure section defines details of the exposure instance to be created.
Key-value pairs in exposure section are:

- name: defines the name of the exposure instance to be created on Oasis.
- do_timestamps: defines timestamps for the upload files. This sub-section, 
  allows the user to either turn it on to be used or turn it off.

There are three main sections under exposure:

- exposure.dict.exposure
- exposure.version.exposure
- exposure.version.correlation

All the above sections have two key-value pairs:

- filename: defines the name of the input file to be uploaded.
- module_supplier_id: defines module supplier id.

**Benchmark**

Benchmark section runs the Benchmark in Oasis after all the input files have
been uploaded. There are four key-value pairs in this section:

- name: defines the name of the Benchmark instance to be created.
- chunk_size: allows user to specify chunk size parameter.
- min_chunk: allows user to specify minimum chunk.
- max_chunk: allows user to specify maximum chunks.

**GUL**

GUL section runs the GUL tasks in Oasis once the Benchmark section is 
successfully executed. There is only one key-value pair in this section:

- name: defines the name of the GUL instance to be created.

**Pubgul**

PubGul section runs once GUL tasks have been successfully executed.
This section essentially publishes the GUL results. Key-value pairs in this
section:

- name: defines the name of the pubgul instance to be created.
- filename: defines the name of the file in which the GUL results will be published.
- module_supplier_id: defines module supplier id.

Example Config Interface Usage
------------------------------
We can run Spittalpond's config interface with the following commands:

.. code:: sh

    $ cd path/to/spittalpond/
    $ python ./spittalpond/config_interface.py ../examples/example.toml

The Spittalpond can also be used interactively after running the config
interface by add the `-i` flag to the `python` command. This allows us to
interrogate the Spittalpond class after it's internal `data_dict` has been
populated.
<!-- TODO: Link to the spittalpond class above -->
In the example interactive Python REPL session below we survey the populated
`Spittalpond.run.data_dict` variable and use data seen to re-create our Ground
Up Losses in Oasis.

.. code:: sh

    $ python -i .\config_interface.py .\example.toml
    You are logged into Mid-tier
    Finished creating model strutures.
    You are logged into Mid-tier
    Finished creating exposure structures.
    Finished benchmark creation.
    You are logged into Mid-tier
    Created GUL data
    You are logged into Mid-tier
    >>> spit = spittalpond_instance
    >>> spit.run.data_dict
    {'version_random': {'job_id': 63, 'taskId': 2}, 'kernel_pubgul': {'download_id_2': u'7', 'download_id': 182, 'job_id': 7
    0, 'taskId': u'7'}, 'kernel_cdf': {'job_id': 65, 'taskId': u'7'}, 'kernel_gul': {'job_id': 67, 'taskId': u'7'}, 'kernel_
    cdfsamples': {'job_id': 66, 'taskId': u'7'}, 'instance_random': {'job_id': 64, 'taskId': u'8'}}
    >>> spit.run.create_gul("example_gul", 7, 10)
    <Response [200]>

.. note::   

    All sections in example.toml are mandatory for an initial run. With
    "initial run" meaning "unpoplated data_dict" But once the data_dict is
    populated, each section can be executed independently. 

.. _here: https://github.com/toml-lang/toml/blob/master/README.md 
.. _example.toml: https://github.com/beckettsimmons/spittalpond/blob/develop/examples/example.toml
.. [1]: Currently, that document is available to Oaiss members at <oasislmf.org>. See page 11 of the document.
