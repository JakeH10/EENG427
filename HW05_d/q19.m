% Author: Jacob Hoffer
% Purpose: Compuational Assistance for Problem 5.19
% Date: 3/25/21

clear; clc;

%% Bullington Position
syms x;
eqn = (1 / 10) * x == (28 / 50) * (300 - x);

dist = solve(eqn, x);

disp(['The Bullington screen is ', num2str(double(dist)),... 
    ' meters from antenna 1.']);

%% Bullington Height

height = (1 / 10) * dist + 10;

disp(['The Bullington screen is ', num2str(double(height)),... 
    ' meters tall.']);

%% Wavelength
lambda = 3e8 / 5e9;

%% Fresnel Parameter
v_F = height * sqrt( (1 / lambda) * ( (1 / dist) + (1 / (300 - dist)) ) );

disp(['The Fresnel parameter is ', num2str(double(v_F))]);

%% Diffraction Attenuation
L = 6.9 + 20 * log10( sqrt((v_F - 0.1)^2 + 1) + v_F - 0.1 );
disp(['The diffraction attenuation is ', num2str(double(L)), ' dB']);