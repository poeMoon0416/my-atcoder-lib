template <typename T>
T lcm(T g, T l) {
  return g*l/gcd(g, l);
}