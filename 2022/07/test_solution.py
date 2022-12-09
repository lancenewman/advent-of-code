import unittest
import solution

from anytree import Node, PostOrderIter


TEST_TERM_OUTPUT_STRING = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class TestSolve(unittest.TestCase):

    def test_from_file(self):
        self.assertEqual((95437, None), solution.solve('test.txt'))


class TestCreateFileTreeFromInput(unittest.TestCase):

    def test_from_string(self):
        expected_root = Node('/', size=48381165)
        a = Node('a', size=94853, parent=expected_root)
        b = Node('b.txt', size=14848514, parent=expected_root)
        c = Node('c.dat', size=8504156, parent=expected_root)
        d = Node('d', size=24933642, parent=expected_root)
        e = Node('e', size=584, parent=a)
        f = Node('f', size=29116, parent=a)
        g = Node('g', size=2557, parent=a)
        h = Node('h.lst', size=62596, parent=a)
        i = Node('i', size=584, parent=e)
        j = Node('j', size=4060174, parent=d)
        dlog = Node('d.log', size=8033020, parent=d)
        dext = Node('d.ext', size=5626152, parent=d)
        k = Node('k', size=7214296, parent=d)

        actual_root = solution.create_file_tree_from_input(TEST_TERM_OUTPUT_STRING.split('\n'))

        for expected, actual in zip(PostOrderIter(expected_root), PostOrderIter(actual_root)):
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.size, actual.size)


class TestExecuteCd(unittest.TestCase):

    def test_cd_to_parent(self):
        parent = Node('parent')
        child = Node('child', parent=parent)
        self.assertEqual(parent.name, solution.execute_cd('..', child).name)

    def test_cd_to_child(self):
        parent = Node('parent')
        child = Node('child', parent=parent)
        self.assertEqual(child.name, solution.execute_cd('child', parent).name)

    def test_cd_to_invalid(self):
        dir = Node('asdf')
        with self.assertRaises(ValueError):
            solution.execute_cd('bad', dir)


class TestGetDirsUnderSize(unittest.TestCase):

    def test_100000k(self):
        expected_root = Node('/', size=48381165)
        a = Node('a', size=94853, parent=expected_root)
        b = Node('b.txt', size=14848514, parent=expected_root)
        c = Node('c.dat', size=8504156, parent=expected_root)
        d = Node('d', size=24933642, parent=expected_root)
        e = Node('e', size=584, parent=a)
        f = Node('f', size=29116, parent=a)
        g = Node('g', size=2557, parent=a)
        h = Node('h.lst', size=62596, parent=a)
        i = Node('i', size=584, parent=e)
        j = Node('j', size=4060174, parent=d)
        dlog = Node('d.log', size=8033020, parent=d)
        dext = Node('d.ext', size=5626152, parent=d)
        k = Node('k', size=7214296, parent=d)

        expected_nodes = [a, e]
        self.assertListEqual(expected_nodes, solution.get_dirs_under_size(expected_root, 100000))


class TestPickDirToDelete(unittest.TestCase):

    def test_from_tree(self):
        root = Node('/', size=48381165)
        a = Node('a', size=94853, parent=root)
        b = Node('b.txt', size=14848514, parent=root)
        c = Node('c.dat', size=8504156, parent=root)
        d = Node('d', size=24933642, parent=root)
        e = Node('e', size=584, parent=a)
        f = Node('f', size=29116, parent=a)
        g = Node('g', size=2557, parent=a)
        h = Node('h.lst', size=62596, parent=a)
        i = Node('i', size=584, parent=e)
        j = Node('j', size=4060174, parent=d)
        dlog = Node('d.log', size=8033020, parent=d)
        dext = Node('d.ext', size=5626152, parent=d)
        k = Node('k', size=7214296, parent=d)

        self.assertEqual(24933642, solution.pick_dir_to_delete(root))