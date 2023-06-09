from behave import *
from test_utils.api_connection import APIConnection
from test_utils.test_bot_commands import TestBotCommands

import time

commands = TestBotCommands()


def before_all(context):
    commands.send_message("-------- **Start of tests** --------")

def before_feature(context, feature):
    time.sleep(0.3)
    commands.send_message(f'**Feature: {feature.name}**')

def before_scenario(context, scenario):
    time.sleep(0.1)
    commands.send_message(f'**Scenario: {scenario.name}**')


def after_scenario(context, scenario):
    APIConnection.delete_all_test_tasks()
    