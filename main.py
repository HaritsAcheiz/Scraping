"""
Earthquake Detection
"""
import eqDetection

if __name__ == '__main__':
    print('Main_Application')
    eq_result = eqDetection.extract()
    eqDetection.view(eq_result)