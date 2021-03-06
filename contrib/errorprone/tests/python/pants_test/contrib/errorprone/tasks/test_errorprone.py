# coding=utf-8
# Copyright 2017 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants_test.jvm.nailgun_task_test_base import NailgunTaskTestBase

from pants.contrib.errorprone.tasks.errorprone import ErrorProne


class ErrorProneTest(NailgunTaskTestBase):
  @classmethod
  def task_type(cls):
    return ErrorProne

  def test_no_sources(self):
    task = self.create_task(self.context())
    self.assertEqual(None, task.execute())
