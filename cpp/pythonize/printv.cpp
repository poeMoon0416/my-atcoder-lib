template <typename T>
void printv(const v<T>& vec) {
  int sz = vec.size();
  if (sz == 0) return;
  for (int i : rng(sz-1)) print(vec[i],"");
  println(vec[sz-1]);
}