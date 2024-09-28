template <typename T>
T input(void) {
  T ret; cin >> ret;
  return ret;
}
template <typename T>
v<T> input(int N) {
  v<T> ret(N); for (T& r : ret) r = input<T>();
  return ret;
}