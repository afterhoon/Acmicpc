h,m = map(int, input().split())
if h == 0:
    if m >= 45:
        m = m - 45
        print(h, m)
    if m < 45:
        h = 23
        m = 60 + (m - 45)
        print(h, m)
if h > 0:
    if m >= 45:
        m = m - 45
        print(h, m)
    if m < 45:
        h = h - 1
        m = 60 + (m - 45)
        print(h, m)

'''
#include
int main(void) {
    int h,m;
    scanf("%d %d", &h, &m);
    if (h == 0) {
        if (m >= 45) {
            m = m - 45;
            printf("%d %d", h, m);
        }
        if (m < 45) {
            h = 23;
            m = 60 + (m - 45);
            printf("%d %d", h, m);
        }
    }
    if (h > 0) {
        if (m >= 45) {
            m = m - 45;
            printf("%d %d", h, m);
        }
        if (m < 45) {
            h = h - 1;
            m = 60 + (m - 45);
            printf("%d %d", h, m);
        }
    }
    return 0;
}
'''