void println(void) {
  cout << endl;
}
template <typename Head, typename... Tail>
void println(Head h, Tail... t) {
  cout << h;
  if (sizeof...(t)) cout << " ";
  println(t...);
}