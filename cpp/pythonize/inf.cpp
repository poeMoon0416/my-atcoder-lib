template<typename T>
T inf(void) {
  return T();
}
template <>
int inf<int>(void) {
  return 1<<30;
}
template <>
lng inf<lng>(void) {
  return lng(1)<<60;
}
template <>
dbl inf<dbl>(void) {
  return DBL_MAX/2;
}