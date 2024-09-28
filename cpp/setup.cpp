////////////////
// ライブラリ //
////////////////

#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/algorithm/string/join.hpp>
#include <atcoder/all>



//////////////
// 名前空間 //
//////////////

using namespace std;
using namespace boost;
using namespace boost::algorithm;
using namespace atcoder;



////////////////////
// 別名(基本の型) //
////////////////////
// typedef int int
typedef long long lng;
typedef double dbl;
// typedef char char
typedef string str;
// typedef bool bool



//////////////////////
// 別名(データ構造) //
//////////////////////

template<typename T>
using v = vector<T>;
template<typename T>
using vv = v<v<T>>;
template<typename T>
using vvv = v<vv<T>>;
template<typename T>
using vvvv = v<vvv<T>>;
template<typename T>
using vvvvv = v<vvvv<T>>;
template<typename T>
using vvvvvv = v<vvvvv<T>>;
template<typename T>
using vvvvvvv = v<vvvvvv<T>>;

template<typename T>
using uset = unordered_set<T>;
template<typename T, typename U>
using umap = unordered_map<T, U>;
// template<typename T>
// using set = set<T>;
// template<typename T, typename U>
// using map = map<T, U>;

template<typename T>
using deq = deque<T>;
template<typename T>
using prq = priority_queue<T>;

using mint = modint;