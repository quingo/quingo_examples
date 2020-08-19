// Name of Experiment: Bell State XW-Measurement v1

OPENQASM 2.0;
include "qelib1.inc";


qreg q[2];
creg c[2];

h q[0];
cx q[0],q[1];
h q[0];
s q[1];
h q[1];
t q[1];
h q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
