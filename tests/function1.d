void f(int fe) {
  Print(fe);
}

void ff() {
 f(34);
}

void g(int a, string b, bool c) {
  Print(c, b, a);

}

int main() {
  f(12);
  ff();
  g(2, " and ",true);
  f(10 + 3 % 2 + 5);
}