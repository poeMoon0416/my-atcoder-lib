v<int> rng(int init, int lim, int step) {
  v<int> ret;
  for (int i : irange(init, lim, step)) {
      ret.push_back(i);
  }
  return ret;
}
v<int> rng(int init, int lim) {
  return rng(init, lim, 1);
}
v<int> rng(int lim) {
  return rng(0, lim, 1);
}