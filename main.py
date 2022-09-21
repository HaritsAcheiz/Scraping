"""
Earthquake Detection
"""
import eqDetection

if __name__ == '__main__':
    print('main_application')
    eq_result = eqDetection.extract()
    eqDetection.view(eq_result)