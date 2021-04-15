f = 2.4e9;
h_t = 10;
d = 100;
h_r = 1.5;


%% Large City
a = 3.2 * (log10(11.75*h_r))^2 - 4.97;
A = 69.55 + 26.16 * log10(f) - 13.82 * log10(h_t) - a;
B = 44.9 - 6.55 * log10(h_t);
C = 0;

L = A + B * log10(d) + C;

disp(['Path Loss: ', num2str(L), ' dB'])

%% Small City
a = (1.1 * log10(f) - 0.7) * h_r - 1.56 * log10(f) + 0.8;
A = 69.55 + 26.16 * log10(f) - 13.82 * log10(h_t) - a;
B = 44.9 - 6.55 * log10(h_t);
C = 0;

L = A + B * log10(d) + C;

disp(['Path Loss: ', num2str(L), ' dB'])

%% Suburban
a = 0;
A = 69.55 + 26.16 * log10(f) - 13.82 * log10(h_t) - a;
B = 44.9 - 6.55 * log10(h_t);
C = -2 * (log10(f / 28))^2 - 5.4;

L = A + B * log10(d) + C;

disp(['Path Loss: ', num2str(L), ' dB'])

%% Suburban
a = 0;
A = 69.55 + 26.16 * log10(f) - 13.82 * log10(h_t) - a;
B = 44.9 - 6.55 * log10(h_t);
C = -4.78 * (log10(f))^2 + 18.33 * log10(f) - 40.94;

L = A + B * log10(d) + C;

disp(['Path Loss: ', num2str(L), ' dB'])