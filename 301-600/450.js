// 450. 删除二叉搜索树中的节点
// 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

// 一般来说，删除节点可分为两个步骤：

// 首先找到需要删除的节点；
// 如果找到了，删除它。
// 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。



var deleteNode = function(root, key) {
    if (root == null) return null
    if (root.val > key ) {
        root.left = deleteNode(root.left, key)
    }  else if (root.val < key) {
        root.right = deleteNode(root.right, key)
    } else {
        if (!root.left && !root.right){
            root = null
        } else if (root.right){
            let last = root.right
            while(last.left){
                last = last.left
            }
            root.val = last.val
            root.right = deleteNode(root.right, last.val)
        } else if (root.left){
            let last = root.left
            while(last.right){
                last = last.right
            }
            root.val = last.val
            root.left = deleteNode(root.left, last.val)
        }
    }
    return root
};