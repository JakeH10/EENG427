function d_p = penetration_depth(f, object)
%PENETRATION_DEPTH find the penetraction depth of an RF wave
%   wavelength: wavelength of the signal
%   f: frequency
%   object: struct
%   d_lf: dielectric loss factor
%   d_p: penetraction depth

e_0 = 8.854e-12;

wavelength = 3e8 / f;

e = object.conductivity / (2 * pi * f);
d_lf = e / (e_0 * object.e_r);

d_p = wavelength / (sqrt(2) * pi * (sqrt(1 + (tan(d_lf))^2) - 1)^(1/2));

end

