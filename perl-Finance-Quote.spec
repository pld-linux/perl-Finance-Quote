#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Finance
%define		pnam	Quote
Summary:	Finance::Quote - Get stock and mutual fund quotes from various exchanges
Summary(pl.UTF-8):	Finance::Quote - Pobieranie notowań giełdowych i funduszy powierniczych
Name:		perl-Finance-Quote
Version:	1.16
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Finance/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	079f20db2a100f63fa03e29beb1e9939
URL:		http://search.cpan.org/dist/Finance-Quote/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(HTML::TableExtract)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module gets stock quotes from various Internet sources, including
Yahoo! Finance, Fidelity Investments, and the Australian Stock
Exchange. There are two methods of using this module - a functional
interface that is depreciated, and an object-orientated method that
provides greater flexibility and stability.

%description -l pl.UTF-8
Ten moduł pobiera notowania giełdowe z różnych źródeł w Internecie, w
tym z Yahoo! Finance, Fidelity Investments i Australian Stock Exchange
(giełdy australijskiej). Istnieją dwie metody użycia tego modułu -
przestarzały interfejs funkcyjny i zorientowana obiektowo metoda
dająca większą elastyczność i stabilność.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%dir %{perl_vendorlib}/Finance
%{perl_vendorlib}/Finance/*.pm
%dir %{perl_vendorlib}/Finance/Quote
%{perl_vendorlib}/Finance/Quote/*.pm
%dir %{perl_vendorlib}/Finance/Quote/Yahoo
%{perl_vendorlib}/Finance/Quote/Yahoo/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
