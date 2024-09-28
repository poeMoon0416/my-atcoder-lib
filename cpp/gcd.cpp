// ユークリッドの互除法と約数集合
template <typename T>
T gcd(T g, T l) {
  if (g < l) swap(g, l);
  T m = g%l;
  while (m != 0) {
    g = l;
    l = m;
    m = g%l;
  }
  return l;
}