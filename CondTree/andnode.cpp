#include "andnode.h"

AndNode::AndNode() :
    OperatorNode()
{
}

bool AndNode::Evaluate(QList<int> values) const
{
    foreach (ConditionTree *child, children) {
        if (!child->Evaluate(values)) { return false; }
    }

    return true;
}
