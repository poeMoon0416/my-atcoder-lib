void print(void) {}
template <typename Head, typename... Tail>
void print(Head h, Tail... t) {
  cout << h;
  if (sizeof...(t)) cout << " ";
  print(t...);
}