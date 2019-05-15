# Stubs for tensorflow.python.debug.lib.session_debug_testlib (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.core.util import event_pb2 as event_pb2
from tensorflow.python.client import session as session
from tensorflow.python.debug.lib import debug_data as debug_data, debug_graphs as debug_graphs, debug_utils as debug_utils
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, errors as errors, ops as ops, test_util as test_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, math_ops as math_ops, parsing_ops as parsing_ops, rnn as rnn, rnn_cell_impl as rnn_cell_impl, state_ops as state_ops, variables as variables
from tensorflow.python.platform import googletest as googletest, test as test
from tensorflow.python.training import gradient_descent as gradient_descent
from typing import Any as Any, Optional as Optional

def no_rewrite_session_config(): ...

class _RNNCellForTest(rnn_cell_impl.RNNCell):
    def __init__(self, input_output_size: Any, state_size: Any) -> None: ...
    @property
    def output_size(self): ...
    @property
    def state_size(self): ...
    def __call__(self, input_: Any, state: Any, scope: Optional[Any] = ...): ...

class SessionDebugTestBase(test_util.TensorFlowTestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def testCopyNodesHaveCorrectDebugOpsAndURLsAttributeValues(self) -> None: ...
    def testConcurrentDumpingToPathsWithOverlappingParentDirsWorks(self) -> None: ...
    def testGetOpTypeWorks(self) -> None: ...
    def testDumpStringTensorsWorks(self) -> None: ...
    def testDumpUninitializedVariable(self) -> None: ...
    def testDebugWhileLoopGeneratesMultipleDumps(self): ...
    def testDebugWhileLoopWatchingWholeGraphWorks(self): ...
    def testDebugTrainingDynamicRNNWorks(self) -> None: ...
    def testDebugCondWatchingWholeGraphWorks(self): ...
    def testFindNodesWithBadTensorValues(self): ...
    def testFindInfOrNanWithOpNameExclusion(self) -> None: ...
    def testGraphStructureLookupGivesDevicesAndNodesInfo(self) -> None: ...
    def testGraphStructureLookupGivesNodesAndAttributes(self) -> None: ...
    def testGraphStructureLookupGivesDebugWatchKeys(self) -> None: ...
    def testGraphStructureLookupGivesNodeInputsAndRecipients(self) -> None: ...
    def testGraphStructureLookupWithoutPartitionGraphsDoesNotErrorOut(self) -> None: ...
    def testGraphPathFindingOnControlEdgesWorks(self) -> None: ...
    def testGraphPathFindingReverseRefEdgeWorks(self) -> None: ...
    def testCausalityCheckOnDumpsDetectsWrongTemporalOrder(self) -> None: ...
    def testWatchingOnlyOneOfTwoOutputSlotsDoesNotLeadToCausalityFailure(self) -> None: ...
    def testOutputSlotWithoutOutgoingEdgeCanBeWatched(self) -> None: ...
    def testWatchingVariableUpdateOpsSeesUpdatedValues(self) -> None: ...
    def testAllowsWatchingUnconnectedOutputTensor(self) -> None: ...
    def testSuccessiveDebuggingRunsIncreasesCounters(self) -> None: ...
    def testDebuggingDuringOpError(self) -> None: ...
    def testDebugNumericSummaryOnInitializedTensorGivesCorrectResult(self) -> None: ...
    def testDebugNumericSummaryOnUninitializedTensorGivesCorrectResult(self) -> None: ...
    def testDebugNumericSummaryFailureIsToleratedWhenOrdered(self) -> None: ...
    def testDebugNumericSummaryInvalidAttributesStringAreCaught(self) -> None: ...
    def testDebugNumericSummaryMuteOnHealthyMutesOnlyHealthyTensorDumps(self) -> None: ...
    def testDebugNumericSummaryMuteOnHealthyAndCustomBoundsWork(self) -> None: ...
    def testDebugQueueOpsDoesNotoErrorOut(self) -> None: ...
    def testLookUpNodePythonTracebackWorks(self) -> None: ...

class DebugConcurrentRunCallsTest(test_util.TensorFlowTestCase):
    def testDebugConcurrentVariableUpdates(self): ...
