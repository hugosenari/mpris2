from mpris2.decorator import DbusMethod

def test_merge_args_get_all_from_std_args():
     args = ()
     std_args = (4, 5, 6)
     assert (4, 5, 6) == DbusMethod.merge_args(args, std_args)

def test_merge_args_get_all_from_args():
     args = (1, 2, 3)
     std_args = ()
     assert (1, 2, 3) == DbusMethod.merge_args(args, std_args)
     
     std_args = (4, 5, 6)
     assert (1, 2, 3) == DbusMethod.merge_args(args, std_args)

def test_merge_args_complete_with_std():
     args = (1, 2)
     std_args = (4, 5, 6)
     assert (1, 2, 6) == DbusMethod.merge_args(args, std_args)

def test_merge_args_both_empty():
     args = ()
     std_args = ()
     assert () == DbusMethod.merge_args(args, std_args)

def test_merge_kwds_get_all_from_std_kwd():
     kwds = {}
     std_kwds = {"a": 4, "b": 5, "c": 6}
     assert std_kwds == DbusMethod.merge_kwds(kwds, std_kwds)

def test_merge_kwds_get_all_from_kwds():
     kwds = {"a": 1, "b": 2, "c": 3}
     std_kwds = {}
     assert {"a": 1, "b": 2, "c": 3} == DbusMethod.merge_kwds(kwds, std_kwds)
     
     std_kwds = {"a": 4, "b": 5, "c": 6}
     assert {"a": 1, "b": 2, "c": 3} == DbusMethod.merge_kwds(kwds, std_kwds)

def test_merge_kwds_complete_with_std():
     kwds = {"a": 1, "b": 2}
     std_kwds = {"a": 4, "b": 5, "c": 6}
     assert {"a": 1, "b": 2, "c": 6} == DbusMethod.merge_kwds(kwds, std_kwds)

def test_merge_kwds_both_empty():
     kwds = {}
     std_kwds = {}
     assert {} == DbusMethod.merge_kwds(kwds, std_kwds)