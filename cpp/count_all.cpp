template <typename T>
umap<T, int> count_all(const v<T>& vec) {
  umap<T, int> ret;
  for (T v : vec) {
    ret[v]++;
  }
  return ret;
}