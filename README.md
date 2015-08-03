# c2raytools_more_examples

I have compiled some of my most important analysis examples that use c2raytools. Here is a possible method of usage:

1) create a *_pyt directory, where * is the simulation name
2) need ../red.dat and ../reds_full.dat (optionally, break into red1,red2,etc.)
3) mkdir results, dT_boxes, dT_pv_boxes
4) run make_dtboxes, xfractions, tau_z
5) after that's completed, run the rest needed mostly get_red_short (for 'interesting' redshifts) followed by coeval_*
6) probably some plotting is in order after that

Some notes:
  make sure the density file path is correct
  make sure the xfrac file path is correct
  some of the routines depend on my c2raytools addons
