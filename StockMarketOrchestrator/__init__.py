import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    apple = yield context.call_activity('AppleFunction', "AAPL")
    amazon = yield context.call_activity('AmazonFunction', apple)
    google = yield context.call_activity('GoogleFunction', amazon)
    writedata = yield context.call_activity('WriteFunction', google)
    return ["Pipeline Completed", f"Apple : {apple[:50]}", f"Amazon : {amazon[:50]}", f"Google : {google[:50]}", writedata]

main = df.Orchestrator.create(orchestrator_function)