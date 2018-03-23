# -*- coding: utf-8 -*-
from aggregator.types import (
    MetricResolver,
    BucketMetricResolver,
)


class TestMetricResolver():

    def test_metric_resolver(self):
        resolver = MetricResolver()

        for mtype, typeclass in resolver.TYPES.iteritems():
            assert resolver[mtype] is not None
            assert resolver[mtype] == typeclass

        resolvable_types = ['c', 'g', 'h']
        resolver.set_resolvable_types(resolvable_types)
        for mtype in resolvable_types:
            assert resolver[mtype] is not None

        assert resolver['foo'] is None

    def test_bucket_metric_resolver(self):
        resolver = BucketMetricResolver()

        for mtype, typeclass in resolver.TYPES.iteritems():
            assert resolver[mtype] is not None
            assert resolver[mtype] == typeclass

        resolvable_types = ['c', 'g', 'h']
        resolver.set_resolvable_types(resolvable_types)
        for mtype in resolvable_types:
            assert resolver[mtype] is not None

        assert resolver['foo'] is None

        resolver.set_resolvable_types(None)
        unresolvable_types = ['ct', 'ct-c', '_dd-r']
        for mtype in unresolvable_types:
            assert resolver[mtype] is None
