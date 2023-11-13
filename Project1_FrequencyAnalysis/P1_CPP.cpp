#include <iostream>

using namespace std;

int main() {

  string s =
      "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd "
      "ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh "
      "but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt "
      "wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj "
      "rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk "
      "nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr "
      "fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr "
      "jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd "
      "ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt "
      "rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru "
      "msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr "
      "riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb";

  char a[2000] = {
      "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd "
      "ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh "
      "but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt "
      "wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj "
      "rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk "
      "nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr "
      "fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr "
      "jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd "
      "ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt "
      "rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru "
      "msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr "
      "riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"};

  int number_of_leaters = 0;
  double A = 0, B = 0, C = 0, D = 0, E = 0, F = 0, G = 0, H = 0, I = 0, J = 0,
         K = 0, L = 0, M = 0, N = 0, O = 0, P = 0, Q = 0, R = 0, S = 0, T = 0,
         U = 0, V = 0, W = 0, X = 0, Y = 0, Z = 0;

  for (int i = 0; i < s.length(); i++) {
    if (a[i] != ' ') {
      number_of_leaters++;
    };
  }

  for (int i = 0; i < s.length(); i++) {
    if (a[i] == 'a') {
      A++;
    }
    if (a[i] == 'b') {
      B++;
    }
    if (a[i] == 'c') {
      C++;
    }
    if (a[i] == 'd') {
      D++;
    }
    if (a[i] == 'e') {
      E++;
    }
    if (a[i] == 'f') {
      F++;
    }
    if (a[i] == 'g') {
      G++;
    }
    if (a[i] == 'h') {
      H++;
    }
    if (a[i] == 'i') {
      I++;
    }
    if (a[i] == 'j') {
      J++;
    }
    if (a[i] == 'k') {
      K++;
    }
    if (a[i] == 'l') {
      L++;
    }
    if (a[i] == 'm') {
      M++;
    }
    if (a[i] == 'n') {
      N++;
    }
    if (a[i] == 'o') {
      O++;
    }
    if (a[i] == 'p') {
      P++;
    }
    if (a[i] == 'q') {
      Q++;
    }
    if (a[i] == 'r') {
      R++;
    }
    if (a[i] == 's') {
      S++;
    }
    if (a[i] == 't') {
      T++;
    }
    if (a[i] == 'u') {
      U++;
    }
    if (a[i] == 'v') {
      V++;
    }
    if (a[i] == 'w') {
      W++;
    }
    if (a[i] == 'x') {
      X++;
    }
    if (a[i] == 'y') {
      Y++;
    }
    if (a[i] == 'z') {
      Z++;
    }
  }

  cout << "a = " << A << " " << (1 * A) / number_of_leaters << endl;
  cout << "b = " << B << " " << (1 * B) / number_of_leaters << endl;
  cout << "c = " << C << " " << (1 * C) / number_of_leaters << endl;
  cout << "d = " << D << " " << (1 * D) / number_of_leaters << endl;
  cout << "e = " << E << " " << (1 * E) / number_of_leaters << endl;
  cout << "f = " << F << " " << (1 * F) / number_of_leaters << endl;
  cout << "g = " << G << " " << (1 * G) / number_of_leaters << endl;
  cout << "h = " << H << " " << (1 * H) / number_of_leaters << endl;
  cout << "i = " << I << " " << (1 * I) / number_of_leaters << endl;
  cout << "j = " << J << " " << (1 * J) / number_of_leaters << endl;
  cout << "k = " << K << " " << (1 * K) / number_of_leaters << endl;
  cout << "l = " << L << " " << (1 * L) / number_of_leaters << endl;
  cout << "m = " << M << " " << (1 * M) / number_of_leaters << endl;
  cout << "n = " << N << " " << (1 * N) / number_of_leaters << endl;
  cout << "o = " << O << " " << (1 * O) / number_of_leaters << endl;
  cout << "p = " << P << " " << (1 * P) / number_of_leaters << endl;
  cout << "q = " << Q << " " << (1 * Q) / number_of_leaters << endl;
  cout << "r = " << R << " " << (1 * R) / number_of_leaters << endl;
  cout << "s = " << S << " " << (1 * S) / number_of_leaters << endl;
  cout << "t = " << T << " " << (1 * T) / number_of_leaters << endl;
  cout << "u = " << U << " " << (1 * U) / number_of_leaters << endl;
  cout << "v = " << V << " " << (1 * V) / number_of_leaters << endl;
  cout << "w = " << W << " " << (1 * W) / number_of_leaters << endl;
  cout << "x = " << X << " " << (1 * X) / number_of_leaters << endl;
  cout << "y = " << Y << " " << (1 * Y) / number_of_leaters << endl;
  cout << "z = " << Z << " " << (1 * Z) / number_of_leaters << endl;

  // char deco[s.length()];
  cout << "before" << endl;
  for (int i = 0; i < s.length(); i++) {
    cout << a[i];
  }

  for (int i = 0; i < s.length(); i++) {
    if (a[i] == 'r') {
      a[i] = 'e';
    } //
    else if (a[i] == 'p') {
      a[i] = 'h';
    } //
    else if (a[i] == 'b') {
      a[i] = 't';
    } //
    else if (a[i] == 'm') {
      a[i] = 'a';
    } //
    else if (a[i] == 'k') {
      a[i] = 'n';
    } //
    else if (a[i] == 'j') {
      a[i] = 'o';
    } //
    else if (a[i] == 'w') {
      a[i] = 'i';
    } //
    else if (a[i] == 'i') {
      a[i] = 's';
    } //
    else if (a[i] == 'u') {
      a[i] = 'r';
    } //
    else if (a[i] == 'h') {
      a[i] = 'l';
    } //
    else if (a[i] == 'd') {
      a[i] = 'd';
    } //
    else if (a[i] == 'v') {
      a[i] = 'c';
    } //
    else if (a[i] == 'x') {
      a[i] = 'f';
    } //
    else if (a[i] == 'y') {
      a[i] = 'm';
    } //
    else if (a[i] == 's') {
      a[i] = 'p';
    } //
    else if (a[i] == 'n') {
      a[i] = 'u';
    } //
    else if (a[i] == 't') {
      a[i] = 'y';
    } //
    else if (a[i] == 'l') {
      a[i] = 'b';
    } //
    else if (a[i] == 'q') {
      a[i] = 'k';
    } //
    else if (a[i] == 'o') {
      a[i] = 'g';
    } //
    else if (a[i] == 'a') {
      a[i] = 'x';
    } //
    else if (a[i] == 'c') {
      a[i] = 'w';
    } //
    else if (a[i] == 'e') {
      a[i] = 'v';
    } //
    else if (a[i] == 'f') {
      a[i] = 'q';
    } //
    else if (a[i] == 'g') {
      a[i] = 'z';
    } //
  }

  cout << endl << endl;

  cout << "after " << endl;
  for (int i = 0; i < s.length(); i++) {
    cout << a[i];
  }

  return 0;
}
