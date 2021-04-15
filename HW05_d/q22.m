% Author: Jacob Hoffer
% Purpose: Compuational Assistance for Problem 5.22
% Date: 3/25/21

clear; clc;

%% Rayleigh Faded Signal
db = [20 6 3];
num = 10 .^ (db ./ 10);

p = 1 - exp(-1./num);