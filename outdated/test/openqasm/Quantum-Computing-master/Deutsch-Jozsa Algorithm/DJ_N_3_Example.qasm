// Name of Experiment: DJ_N_3_Example

OPENQASM 2.0;
include "qelib1.inc";

h q[0];
h q[1];
h q[2];
h q[2];
z q[0];
cx q[1], q[2];
h q[2];
h q[0];
h q[1];
h q[2];
measure q[0];
measure q[1];
measure q[2];
