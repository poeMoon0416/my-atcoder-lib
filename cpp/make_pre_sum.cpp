template <typename T>
v<T> make_pre_sum(const v<T>& src) {
  int sz = src.size();
  v<T> pre_sum(sz+1);
  pre_sum[0] = 0;
  for (int i : rng(1, sz+1)) {
    pre_sum[i] = pre_sum[i-1]+src[i-1];
  }
  return pre_sum;
}