============================
stepfunctions-start-execution-task
============================

.. _APL2: http://www.apache.org/licenses/LICENSE-2.0.txt

Starts an AWS step-function execution

AWS Permissions Required
------------------------
- states:StartExecution

Handler Method
--------------
.. code::

  function.handler

Request Syntax
--------------
.. code::

  {
      "StateMachineArn": "string",
      "Name": "string",
      "Input": {}
  }

**StateMachineArn**
  The Amazon Resource Name (ARN) of the state
  machine to execute.
**Name**
  The name of the execution.
**Input**
  The map that contains the input data for the execution.

Response syntax
---------------
.. code::

  {
      "executionArn": "string",
      "startDate": "iso8601 format date/time"
  }

Lambda Package Location
-----------------------
https://s3.amazonaws.com/lambdalambdalambda-repo/quinovas/stepfunctions-start-execution-task/stepfunctions-start-execution-task-0.0.1.zip

License: `APL2`_
