#
# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define         module  flask-login
Summary:	Flask-Login provides user session management for Flask
Summary(pl.UTF-8):	Wsparcie dla zarzadzania sesja uzytkownika w aplikacjach Flask
Name:		python-%{module}
Version:	0.2.11
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/F/Flask-Login/Flask-Login-%{version}.tar.gz
# Source0-md5:	c0a7eaf28623f0aeac4929dc05a7a064
URL:		https://github.com/maxcountryman/flask-login/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

%description -l pl.UTF-8
Wsparcie dla zarzadzania sesja uzytkownika w aplikacjach Flask. Plugin
obsluguje najpopularniejsze przypadki uzycia: logowanie, wylogowanie,
zapamietywanie sesji uzytkownikow przez okreslony czas.

%package -n python3-%{module}
Summary:	Flask-Login provides user session management for Flask
Summary(pl.UTF-8):	Wsparcie dla zarzadzania sesja uzytkownika w aplikacjach Flask
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

%description -n python3-%{module} -l pl.UTF-8
Wsparcie dla zarzadzania sesja uzytkownika w aplikacjach Flask. Plugin
obsluguje najpopularniejsze przypadki uzycia: logowanie, wylogowanie,
zapamietywanie sesji uzytkownikow przez okreslony czas.

%prep
%setup -q -n Flask-Login-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.markdown LICENSE
%{py_sitescriptdir}/flask_login.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Flask_Login-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.markdown LICENSE
%{py3_sitescriptdir}/flask_login.py
%{py3_sitescriptdir}/__pycache__/flask_login.*.py[co]
%{py3_sitescriptdir}/Flask_Login-%{version}-py*.egg-info
%endif

